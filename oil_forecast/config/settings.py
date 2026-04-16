import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()

DEFAULT_DATA_PATH = "crude-oil-prices.csv"


@dataclass(frozen=True)
class Settings:
    data_path: str = os.getenv("DATA_PATH", DEFAULT_DATA_PATH)
    output_dir: str = os.getenv("OUTPUT_DIR", "outputs")
    forecast_steps: int = int(os.getenv("FORECAST_STEPS", "12"))
    arima_order: tuple[int, int, int] = (
        int(os.getenv("ARIMA_P", "1")),
        int(os.getenv("ARIMA_D", "1")),
        int(os.getenv("ARIMA_Q", "1")),
    )
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
