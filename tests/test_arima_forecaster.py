import unittest

import pandas as pd

from oil_forecast.models.arima_forecaster import ArimaForecaster
from oil_forecast.utils.data_pipeline import load_oil_data


class TestArimaForecaster(unittest.TestCase):
    def test_forecast_length(self):
        series = load_oil_data("crude-oil-prices.csv")["oil_price"]
        model = ArimaForecaster(order=(1, 1, 1)).fit(series)
        result = model.forecast(3)
        self.assertEqual(len(result.forecast), 3)
        self.assertIsInstance(result.forecast, pd.Series)


if __name__ == "__main__":
    unittest.main()
