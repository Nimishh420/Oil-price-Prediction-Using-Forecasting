from __future__ import annotations

import logging

from oil_forecast.config.settings import Settings
from oil_forecast.models.arima_forecaster import ArimaForecaster
from oil_forecast.utils.data_pipeline import build_forecast_frame, load_oil_data
from oil_forecast.utils.exporters import export_for_power_bi
from oil_forecast.utils.logging_config import configure_logging


def run_pipeline(settings: Settings | None = None) -> dict[str, str]:
    settings = settings or Settings()
    configure_logging(settings.log_level)
    logger = logging.getLogger(__name__)

    logger.info("Loading oil data from %s", settings.data_path)
    history = load_oil_data(settings.data_path)

    forecaster = ArimaForecaster(order=settings.arima_order).fit(history["oil_price"])
    forecast = forecaster.forecast(settings.forecast_steps)
    output_df = build_forecast_frame(history, forecast.forecast)

    export_paths = export_for_power_bi(output_df, settings.output_dir)
    logger.info("Forecast exported: %s", export_paths)
    return export_paths


if __name__ == "__main__":
    run_pipeline()
