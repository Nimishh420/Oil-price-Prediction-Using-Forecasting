# Oil Price Prediction Using Forecasting

Production-ready ARIMA forecasting for crude oil prices with API and Power BI export support.

## Project structure

- `main.py`: Runs the forecast pipeline and exports outputs.
- `api.py`: Flask API with `/health` and `/predict` endpoints.
- `oil_forecast/`: Modular package (`config`, `models`, `utils`).
- `tests/`: Unit tests for pipeline, model, and API.

## Quick start

```bash
python -m pip install -r requirements.txt
python main.py
python api.py
```

## Configuration

Copy `.env.example` to `.env` and adjust values:

- `DATA_PATH`
- `OUTPUT_DIR`
- `FORECAST_STEPS`
- `ARIMA_P`, `ARIMA_D`, `ARIMA_Q`
- `LOG_LEVEL`

## API

- `GET /health`
- `GET /predict?steps=12`

Example response:

```json
{
  "predictions": [
    {"year": 2024, "predicted_oil_price": 70.1}
  ]
}
```

## Power BI integration

Run `python main.py` to generate:

- `outputs/oil_price_forecast.csv`
- `outputs/oil_price_forecast.xlsx`
- `outputs/oil_price_forecast.json`

In Power BI Desktop:
1. **Get Data** → CSV or Excel.
2. Select output file from `outputs/`.
3. Create visuals (line chart by `year`, card for average `predicted_oil_price`).
4. Refresh data after each pipeline run.

## Docker

```bash
docker compose up --build
```

API will be available at `http://localhost:8000`.

## CI and quality

- GitHub Actions workflow: `.github/workflows/ci.yml`
- Pre-commit hooks: `.pre-commit-config.yaml`
- Unit tests: `python -m unittest discover -s tests -p 'test_*.py' -v`
