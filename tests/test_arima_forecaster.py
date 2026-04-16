import unittest

import numpy as np
import pandas as pd

from oil_forecast.models.arima_forecaster import ArimaForecaster


class TestArimaForecaster(unittest.TestCase):
    def test_forecast_length(self):
        series = pd.Series(np.linspace(10, 50, 30))
        model = ArimaForecaster(order=(1, 1, 1)).fit(series)
        result = model.forecast(3)
        self.assertEqual(len(result.forecast), 3)
        self.assertIsInstance(result.forecast, pd.Series)


if __name__ == "__main__":
    unittest.main()
