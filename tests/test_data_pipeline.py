import unittest
from tempfile import NamedTemporaryFile

import pandas as pd
from oil_forecast.utils.data_pipeline import build_forecast_frame, load_oil_data


class TestDataPipeline(unittest.TestCase):
    def test_load_oil_data_has_expected_columns(self):
        raw = pd.DataFrame(
            {
                "Year": [2020, 2021, 2022],
                "Oil price - Crude prices since 1861 (current US$)": [40.0, 55.0, 70.0],
            }
        )
        with NamedTemporaryFile(mode="w", suffix=".csv") as temp_file:
            raw.to_csv(temp_file.name, index=False)
            df = load_oil_data(temp_file.name)
        self.assertIn("year", df.columns)
        self.assertIn("oil_price", df.columns)
        self.assertGreater(len(df), 0)

    def test_build_forecast_frame_generates_next_years(self):
        history = pd.DataFrame({"year": [2020, 2021, 2022], "oil_price": [40.0, 55.0, 70.0]})
        output = build_forecast_frame(history, history["oil_price"].reset_index(drop=True))
        self.assertEqual(output["year"].iloc[0], history["year"].iloc[-1] + 1)


if __name__ == "__main__":
    unittest.main()
