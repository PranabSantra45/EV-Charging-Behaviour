from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import pandas as pd

app = Flask(__name__)
CORS(app)

# Load new model
model = pickle.load(open("energy_model_v2.pkl", "rb"))

@app.route("/")
def home():
    return "Energy Prediction API Running (v2)"

@app.route("/predict_energy", methods=["POST"])
def predict_energy():
    try:
        data = request.json

        # Compute derived feature
        energy_expected = (
            (float(data["soc_end"]) - float(data["soc_start"])) / 100
        ) * float(data["battery_capacity"])

        input_data = {
            "hour_of_day": float(data["time"]),
            "day_of_week": data["day"],
            "charging_duration_minutes": float(data["duration"]),
            "battery_capacity_(kwh)": float(data["battery_capacity"]),
            "state_of_charge_(start_%)": float(data["soc_start"]),
            "state_of_charge_(end_%)": float(data["soc_end"]),
            "charging_rate_(kw)": float(data["charging_rate"]),
            "temperature_c": float(data["temperature"]),
            "charger_type": data["charger_type"],
            "location_type": data["location_type"],
            "vehicle_model": data["vehicle_model"],
            "energy_expected": energy_expected
        }

        df = pd.DataFrame([input_data])

        prediction = model.predict(df)[0]

        return jsonify({
            "energy": round(float(prediction), 2)
        })

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)