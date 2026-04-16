from __future__ import annotations

from flask import Flask, jsonify, request

from oil_forecast.config.settings import Settings
from oil_forecast.models.arima_forecaster import ArimaForecaster
from oil_forecast.utils.data_pipeline import build_forecast_frame, load_oil_data


def create_app() -> Flask:
    app = Flask(__name__)

    @app.get("/health")
    def health() -> tuple[dict[str, str], int]:
        return {"status": "ok"}, 200

    @app.get("/predict")
    def predict() -> tuple[dict, int]:
        settings = Settings()
        steps = request.args.get("steps", default=settings.forecast_steps, type=int)
        if not steps or steps <= 0:
            return {"error": "steps must be a positive integer"}, 400

        history = load_oil_data(settings.data_path)
        model = ArimaForecaster(order=settings.arima_order).fit(history["oil_price"])
        forecast = model.forecast(steps)
        output = build_forecast_frame(history, forecast.forecast)
        return jsonify({"predictions": output.to_dict(orient="records")}), 200

    return app


app = create_app()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
