from app import extract_predictions, normalise_label


def test_normalise_label_variants():
    assert normalise_label("Giant Hogweed") == "giant_hogweed"
    assert normalise_label("Heracleum sphondylium") == "common_hogweed"
    assert normalise_label("cow-parsley") == "cow_parsley"


def test_extract_predictions_list_shape():
    payload = {
        "predictions": [
            {"class": "giant_hogweed", "confidence": 0.91},
            {"class": "common_hogweed", "confidence": 0.07},
        ]
    }
    assert extract_predictions(payload)[0] == ("giant_hogweed", 0.91)


def test_extract_predictions_mapping_shape():
    payload = {"predictions": {"cow_parsley": 0.8, "common_hogweed": 0.2}}
    assert extract_predictions(payload)[0] == ("cow_parsley", 0.8)


def test_extract_predictions_top_shape():
    payload = {"top": "Common Hogweed", "confidence": 0.76}
    assert extract_predictions(payload) == [("common_hogweed", 0.76)]


def test_extract_predictions_workflow_shape():
    payload = [
        {
            "classification": {
                "predictions": [
                    {"class": "giant_hogweed", "class_id": 1, "confidence": 0.93}
                ]
            }
        }
    ]
    assert extract_predictions(payload) == [("giant_hogweed", 0.93)]
