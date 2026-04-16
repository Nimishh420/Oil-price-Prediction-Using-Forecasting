import unittest

from oil_forecast.utils.data_pipeline import build_forecast_frame, load_oil_data


class TestDataPipeline(unittest.TestCase):
    def test_load_oil_data_has_expected_columns(self):
        df = load_oil_data("crude-oil-prices.csv")
        self.assertIn("year", df.columns)
        self.assertIn("oil_price", df.columns)
        self.assertGreater(len(df), 0)

    def test_build_forecast_frame_generates_next_years(self):
        history = load_oil_data("crude-oil-prices.csv").tail(3)
        output = build_forecast_frame(history, history["oil_price"].reset_index(drop=True))
        self.assertEqual(output["year"].iloc[0], history["year"].iloc[-1] + 1)


if __name__ == "__main__":
    unittest.main()
