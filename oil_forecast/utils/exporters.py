from __future__ import annotations

import json
from pathlib import Path

import pandas as pd


def export_for_power_bi(df: pd.DataFrame, output_dir: str) -> dict[str, str]:
    target = Path(output_dir)
    target.mkdir(parents=True, exist_ok=True)

    csv_path = target / "oil_price_forecast.csv"
    xlsx_path = target / "oil_price_forecast.xlsx"
    json_path = target / "oil_price_forecast.json"

    df.to_csv(csv_path, index=False)
    df.to_excel(xlsx_path, index=False)
    with json_path.open("w", encoding="utf-8") as handle:
        json.dump(df.to_dict(orient="records"), handle, indent=2)

    return {
        "csv": str(csv_path),
        "excel": str(xlsx_path),
        "json": str(json_path),
    }
