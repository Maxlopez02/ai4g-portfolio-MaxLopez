"""Curated public information used to ground MigrationHelp answers.

The app deliberately does not search the open web. Each source below is an official
Dutch public-service page, reviewed for this prototype on 23 September 2026.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Source:
    id: str
    title: str
    organisation: str
    url: str
    last_checked: str
    topics: tuple[str, ...]
    facts: tuple[str, ...]


SOURCES: tuple[Source, ...] = (
    Source(
        id="government-moving",
        title="What do I need to arrange if I'm moving to the Netherlands?",
        organisation="Government of the Netherlands",
        url="https://www.government.nl/faq/what-do-i-need-to-arrange-if-im-moving-to-the-netherlands",
        last_checked="2026-09-23",
        topics=("arrival", "registration", "bsn", "health insurance", "gp", "tax", "benefits", "digid"),
        facts=(
            "A person staying for more than four months must register with the municipality where they live, within five days after arrival.",
            "Municipal registration creates a BRP record and a citizen service number (BSN).",
            "A person staying no more than four months can register as a non-resident in the BRP (RNI).",
            "People who live in the Netherlands generally need Dutch health insurance and are advised to find a general practitioner.",
            "DigiD is used for online contact with Dutch public bodies.",
        ),
    ),
    Source(
        id="government-brp",
        title="When should I register with the Personal Records Database as a resident?",
        organisation="Government of the Netherlands",
        url="https://www.government.nl/faq/when-should-i-register-with-the-personal-records-database-as-a-resident",
        last_checked="2026-09-23",
        topics=("registration", "municipality", "brp", "bsn", "address"),
        facts=(
            "People living in the Netherlands for longer than four months must register as residents in the BRP.",
            "Registration is normally at the permanent home address; a correspondence address can apply in specified situations.",
            "Partners and children who also moved must attend the municipality appointment.",
            "A BSN is issued on registration and is used for government contact, care and tax matters.",
        ),
    ),
    Source(
        id="government-digid",
        title="Applying for a DigiD",
        organisation="Government of the Netherlands",
        url="https://www.government.nl/themes/government-and-democracy/online-access-to-public-services-european-economic-area-eidas/digid/digid-applications-from-the-netherlands",
        last_checked="2026-09-23",
        topics=("digid", "online", "identity", "brp", "government"),
        facts=(
            "A person applying for DigiD from within the Netherlands must be registered in the BRP.",
            "DigiD is a digital identity for accessing Dutch public services online.",
        ),
    ),
    Source(
        id="government-insurance",
        title="When do I need compulsory health insurance if I come to live or work in the Netherlands?",
        organisation="Government of the Netherlands",
        url="https://www.government.nl/faq/health-insurance/when-do-i-need-to-take-out-health-insurance-if-i-come-to-live-in-the-netherlands",
        last_checked="2026-09-23",
        topics=("health", "insurance", "work", "gp", "care"),
        facts=(
            "People who come to live or work in the Netherlands should arrange Dutch health insurance as quickly as possible when the Dutch insurance rules apply to them.",
            "The official page says to register with a Dutch municipality as part of the process.",
            "Individual exceptions exist, so a person's insurer or the CAK should confirm case-specific coverage.",
        ),
    ),
    Source(
        id="ind-living",
        title="Living in the Netherlands with a residence permit",
        organisation="Immigration and Naturalisation Service (IND)",
        url="https://ind.nl/en/living-in-the-netherlands-with-a-residence-permit/living-in-the-netherlands",
        last_checked="2026-09-23",
        topics=("residence permit", "ind", "registration", "insurance", "tb", "integration", "work"),
        facts=(
            "IND lists municipal registration, possible TB testing, healthcare insurance, schooling, civic integration and legal obligations among post-arrival matters.",
            "Residence-permit holders must keep their main residence in the Netherlands and report relevant changes where required.",
            "The exact obligations depend on the person's permit and situation; the official IND page or an IND adviser must be used for a decision about a specific case.",
        ),
    ),
    Source(
        id="ind-home",
        title="How can we help you?",
        organisation="Immigration and Naturalisation Service (IND)",
        url="https://ind.nl/en",
        last_checked="2026-09-23",
        topics=("residence permit", "application", "appointment", "biometrics", "status", "ind", "citizenship"),
        facts=(
            "IND provides official information about applying for, extending and changing residence permits.",
            "IND offers appointment booking, application-status information and a navigation guide.",
            "Asylum and case-specific residence decisions are outside this chatbot's scope and should be handled with IND or a qualified adviser.",
        ),
    ),
)


SOURCE_BY_ID = {source.id: source for source in SOURCES}


TOPIC_ALIASES: dict[str, tuple[str, ...]] = {
    "registration": ("register", "registration", "municipality", "gemeente", "brp", "bsn", "address", "inschrijven"),
    "digid": ("digid", "digital identity", "online government", "inloggen"),
    "health": ("health", "insurance", "doctor", "hospital", "gp", "zorg", "arts", "verzekering"),
    "residence permit": ("permit", "visa", "ind", "residence", "biometric", "verblijfsvergunning", "application status"),
    "arrival": ("arrive", "arrival", "move", "moving", "first", "new", "aankomst", "verhuizen"),
}


def select_sources(question: str, limit: int = 4) -> list[Source]:
    """Return relevant sources with a deterministic keyword score.

    A general moving guide is always available as a baseline. This retrieval step
    keeps the model's context small and makes its evidence inspectable.
    """

    normalised = question.casefold()
    expanded_terms: set[str] = set(normalised.split())
    for topic, aliases in TOPIC_ALIASES.items():
        if any(alias in normalised for alias in aliases):
            expanded_terms.add(topic)
            expanded_terms.update(aliases)

    scored: list[tuple[int, Source]] = []
    for source in SOURCES:
        haystack = " ".join((*source.topics, *source.facts)).casefold()
        score = sum(1 for term in expanded_terms if len(term) > 2 and term in haystack)
        if source.id == "government-moving":
            score += 1
        scored.append((score, source))

    scored.sort(key=lambda item: item[0], reverse=True)
    chosen = [source for score, source in scored if score > 0][:limit]
    return chosen or [SOURCE_BY_ID["government-moving"]]


def format_source_context(sources: list[Source]) -> str:
    sections = []
    for source in sources:
        facts = "\n".join(f"- {fact}" for fact in source.facts)
        sections.append(
            f"SOURCE_ID: {source.id}\n"
            f"TITLE: {source.title}\n"
            f"ORGANISATION: {source.organisation}\n"
            f"URL: {source.url}\n"
            f"LAST_CHECKED: {source.last_checked}\n"
            f"VERIFIED_FACTS:\n{facts}"
        )
    return "\n\n".join(sections)
