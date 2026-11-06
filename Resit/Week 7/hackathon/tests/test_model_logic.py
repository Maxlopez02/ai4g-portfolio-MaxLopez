import unittest

from model_logic import extract_predictions, normalise_label, screening_decision


class ModelLogicTests(unittest.TestCase):
    def test_normalises_scientific_name(self):
        self.assertEqual(
            normalise_label("Heracleum mantegazzianum"), "giant_hogweed"
        )

    def test_parses_and_sorts_score_mapping(self):
        payload = {
            "predictions": {"cow parsley": 0.12, "giant hogweed": 0.88}
        }
        self.assertEqual(
            extract_predictions(payload),
            [("giant_hogweed", 0.88), ("cow_parsley", 0.12)],
        )

    def test_low_confidence_is_withheld(self):
        self.assertEqual(
            screening_decision([("giant_hogweed", 0.64)], threshold=0.65),
            ("uncertain", 0.64),
        )

    def test_threshold_result_is_returned(self):
        self.assertEqual(
            screening_decision([("common_hogweed", 0.65)], threshold=0.65),
            ("common_hogweed", 0.65),
        )


if __name__ == "__main__":
    unittest.main()
