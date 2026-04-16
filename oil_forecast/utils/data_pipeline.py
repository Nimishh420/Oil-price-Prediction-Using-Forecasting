from __future__ import annotations

import pandas as pd

YEAR_COLUMN = "Year"
PRICE_COLUMN = "Oil price - Crude prices since 1861 (current US$)"


def load_oil_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    missing = {YEAR_COLUMN, PRICE_COLUMN}.difference(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    cleaned = (
        df[[YEAR_COLUMN, PRICE_COLUMN]]
        .rename(columns={YEAR_COLUMN: "year", PRICE_COLUMN: "oil_price"})
        .dropna()
        .sort_values("year")
        .reset_index(drop=True)
    )
    cleaned["year"] = cleaned["year"].astype(int)
    cleaned["oil_price"] = cleaned["oil_price"].astype(float)
    return cleaned


def build_forecast_frame(history: pd.DataFrame, forecast_values: pd.Series) -> pd.DataFrame:
    last_year = int(history["year"].iloc[-1])
    forecast_years = range(last_year + 1, last_year + 1 + len(forecast_values))
    return pd.DataFrame(
        {
            "year": list(forecast_years),
            "predicted_oil_price": forecast_values.astype(float),
        }
    )
