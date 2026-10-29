#!/usr/bin/env python3
"""Download a licence-tracked Dutch plant image dataset from the GBIF API.

Images are intentionally excluded from Git. The committed CSV preserves provenance.
The held-out test folder must not be uploaded to Roboflow before final evaluation.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import math
import random
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from PIL import Image, ImageOps

GBIF_API = "https://api.gbif.org/v1/occurrence/search"
USER_AGENT = "HogweedGuardNL/1.0 (educational SDG 15 project; GBIF-attributed download)"

SPECIES = {
    "giant_hogweed": {
        "taxon_key": 3034825,
        "scientific_name": "Heracleum mantegazzianum",
    },
    "common_hogweed": {
        "taxon_key": 3034830,
        "scientific_name": "Heracleum sphondylium",
    },
    "cow_parsley": {
        "taxon_key": 5371742,
        "scientific_name": "Anthriscus sylvestris",
    },
}

ALLOWED_LICENCE_MARKERS = (
    "creativecommons.org/publicdomain/zero",
    "creativecommons.org/licenses/by/",
    "creativecommons.org/licenses/by-nc/",
    "creativecommons.org/licenses/by-sa/",
    "creativecommons.org/licenses/by-nc-sa/",
)

FIELDS = [
    "class_label",
    "split",
    "file_name",
    "sha256",
    "gbif_key",
    "scientific_name",
    "event_date",
    "locality",
    "country_code",
    "creator",
    "rights_holder",
    "licence",
    "image_url",
    "gbif_record_url",
    "publisher",
]


def fetch_json(url: str) -> dict[str, Any]:
    request = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    with urlopen(request, timeout=35) as response:
        return json.load(response)


def get_bytes(url: str) -> bytes:
    request = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "image/*"})
    with urlopen(request, timeout=40) as response:
        content_type = response.headers.get("Content-Type", "")
        if "image" not in content_type.lower():
            raise ValueError(f"Not an image response: {content_type}")
        content = response.read(18_000_001)
        if len(content) > 18_000_000:
            raise ValueError("Image exceeds the 18 MB download limit")
        return content


def licence_allowed(value: str) -> bool:
    lowered = value.lower().replace("legalcode", "")
    return any(marker in lowered for marker in ALLOWED_LICENCE_MARKERS)


def split_for(record: dict[str, Any]) -> str:
    """Keep a deterministic 10% hold-out set, grouped roughly by photographer."""
    group = (
        record.get("recordedBy")
        or record.get("identifiedBy")
        or record.get("publishingOrgKey")
        or str(record.get("key"))
    )
    bucket = int(hashlib.sha256(str(group).encode("utf-8")).hexdigest()[:8], 16) % 10
    return "test" if bucket < 2 else "development"


def media_candidates(record: dict[str, Any]) -> list[dict[str, Any]]:
    candidates: list[dict[str, Any]] = []
    record_licence = str(record.get("license") or "")
    for media in record.get("media", []):
        if str(media.get("type", "")).lower() != "stillimage":
            continue
        url = media.get("identifier") or media.get("references")
        licence = str(media.get("license") or record_licence)
        if url and licence_allowed(licence):
            candidates.append({**media, "download_url": url, "resolved_licence": licence})
    return candidates


def prepare_jpeg(content: bytes) -> tuple[bytes, str]:
    with Image.open(io.BytesIO(content)) as source:
        image = ImageOps.exif_transpose(source).convert("RGB")
        image.thumbnail((1280, 1280), Image.Resampling.LANCZOS)
        output = io.BytesIO()
        image.save(output, "JPEG", quality=88, optimize=True)
    prepared = output.getvalue()
    return prepared, hashlib.sha256(prepared).hexdigest()


def download_candidate(candidate: tuple[dict[str, Any], dict[str, Any], str]):
    record, media, split = candidate
    content = get_bytes(str(media["download_url"]))
    prepared, digest = prepare_jpeg(content)
    return record, media, split, prepared, digest


def search_records(taxon_key: int, max_pages: int = 20) -> list[dict[str, Any]]:
    def fetch_page(page: int) -> dict[str, Any]:
        params = {
            "taxon_key": taxon_key,
            "country": "NL",
            "media_type": "StillImage",
            "occurrence_status": "PRESENT",
            "limit": 300,
            "offset": page * 300,
        }
        return fetch_json(f"{GBIF_API}?{urlencode(params)}")

    first = fetch_page(0)
    records: list[dict[str, Any]] = list(first.get("results", []))
    page_count = min(max_pages, math.ceil(int(first.get("count", 0)) / 300))
    with ThreadPoolExecutor(max_workers=10) as pool:
        futures = [pool.submit(fetch_page, page) for page in range(1, page_count)]
        for future in as_completed(futures):
            try:
                records.extend(future.result().get("results", []))
            except Exception as exc:
                print(f"skip GBIF result page: {exc}", flush=True)
    return records


def download_class(
    root: Path,
    class_label: str,
    settings: dict[str, Any],
    development_target: int,
    test_target: int,
    seed: int,
) -> list[dict[str, str]]:
    records = search_records(settings["taxon_key"])
    random.Random(seed + settings["taxon_key"]).shuffle(records)
    accepted: Counter[str] = Counter()
    rows: list[dict[str, str]] = []
    seen_urls: set[str] = set()
    seen_hashes: set[str] = set()
    targets = {"development": development_target, "test": test_target}

    candidate_lists: dict[str, list[tuple[dict[str, Any], dict[str, Any], str]]] = {
        "development": [],
        "test": [],
    }
    for record in records:
        split = split_for(record)
        for media in media_candidates(record):
            url = str(media["download_url"])
            if url in seen_urls:
                continue
            seen_urls.add(url)
            candidate_lists[split].append((record, media, split))
            break

    # Use bounded candidate pools so downloads finish in minutes rather than serially.
    candidates = (
        candidate_lists["development"][: development_target * 6]
        + candidate_lists["test"][: test_target * 15]
    )
    with ThreadPoolExecutor(max_workers=12) as pool:
        futures = [pool.submit(download_candidate, candidate) for candidate in candidates]
        for future in as_completed(futures):
            try:
                record, media, split, prepared, digest = future.result()
            except Exception as exc:
                print(f"skip {class_label}: {exc}")
                continue
            if accepted[split] >= targets[split] or digest in seen_hashes:
                continue
            seen_hashes.add(digest)
            accepted[split] += 1
            target_root = "held_out_test" if split == "test" else "roboflow_upload"
            filename = f"{class_label}_{record.get('key')}_{accepted[split]:03d}.jpg"
            destination = root / "images" / target_root / class_label / filename
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(prepared)

            creator = str(media.get("creator") or record.get("recordedBy") or "Not supplied")
            rights_holder = str(media.get("rightsHolder") or record.get("rightsHolder") or creator)
            rows.append(
                {
                    "class_label": class_label,
                    "split": split,
                    "file_name": filename,
                    "sha256": digest,
                    "gbif_key": str(record.get("key", "")),
                    "scientific_name": str(record.get("scientificName") or settings["scientific_name"]),
                    "event_date": str(record.get("eventDate") or "Not supplied"),
                    "locality": str(record.get("locality") or record.get("stateProvince") or "Netherlands"),
                    "country_code": str(record.get("countryCode") or "NL"),
                    "creator": creator,
                    "rights_holder": rights_holder,
                    "licence": str(media["resolved_licence"]),
                    "image_url": str(media["download_url"]),
                    "gbif_record_url": f"https://www.gbif.org/occurrence/{record.get('key')}",
                    "publisher": str(record.get("publishingOrgKey") or record.get("datasetTitle") or "GBIF contributor"),
                }
            )
            print(
                f"saved {class_label}: {accepted['development']}/{development_target} dev, "
                f"{accepted['test']}/{test_target} test",
                flush=True,
            )
            if all(accepted[name] >= target for name, target in targets.items()):
                for pending in futures:
                    pending.cancel()
                break

    if not all(accepted[name] >= target for name, target in targets.items()):
        raise RuntimeError(f"Not enough usable {class_label} images: {dict(accepted)}")
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parents[1] / "dataset")
    parser.add_argument("--development-per-class", type=int, default=108)
    parser.add_argument("--test-per-class", type=int, default=12)
    parser.add_argument("--seed", type=int, default=20261029)
    args = parser.parse_args()

    args.output.mkdir(parents=True, exist_ok=True)
    rows: list[dict[str, str]] = []
    for class_label, settings in SPECIES.items():
        rows.extend(
            download_class(
                args.output,
                class_label,
                settings,
                args.development_per_class,
                args.test_per_class,
                args.seed,
            )
        )

    metadata_path = args.output / "metadata.csv"
    with metadata_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)

    report = {
        "source": "GBIF occurrence API",
        "country_filter": "NL",
        "development_images_for_roboflow": args.development_per_class * len(SPECIES),
        "held_out_test_images": args.test_per_class * len(SPECIES),
        "total_images": len(rows),
        "classes": list(SPECIES),
        "seed": args.seed,
        "important": "Do not upload dataset/images/held_out_test to Roboflow before final evaluation.",
    }
    (args.output / "download_report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
