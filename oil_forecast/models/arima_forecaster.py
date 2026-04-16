from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

import numpy as np
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA


@dataclass
class ForecastResult:
    forecast: pd.Series


class ArimaForecaster:
    """Wrapper around statsmodels ARIMA for oil price forecasting."""

    def __init__(self, order: tuple[int, int, int] = (1, 1, 1)) -> None:
        self.order = order
        self._fit_result = None

    def fit(self, values: Iterable[float]) -> "ArimaForecaster":
        series = np.asarray(list(values), dtype="float64")
        if series.size < 5:
            raise ValueError("At least 5 observations are required to train ARIMA")
        model = ARIMA(series, order=self.order)
        self._fit_result = model.fit()
        return self

    def forecast(self, steps: int) -> ForecastResult:
        if self._fit_result is None:
            raise RuntimeError("Model must be fit before forecasting")
        if steps <= 0:
            raise ValueError("steps must be greater than zero")
        forecast_values = self._fit_result.forecast(steps=steps)
        return ForecastResult(forecast=pd.Series(forecast_values).reset_index(drop=True))
