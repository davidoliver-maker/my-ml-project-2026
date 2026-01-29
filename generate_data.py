import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

ASSET_NAMES = ["Gearbox_1", "Compressor_A", "Pump_B", "Turbine_X", "Motor_5"]
DAYS = 90
HOURS_PER_DAY = 24
START_DATE = datetime(2025, 7, 1)

SENSORS = {
    "temperature":   {"base": 58,   "noise": 4.5,  "drift_per_day": [0.10, 0.14, 0.07, 0.18, 0.09]},
    "vibration":     {"base": 1.1,  "noise": 0.35, "drift_per_day": [0.012, 0.020, 0.009, 0.028, 0.016]},
    "oil_quality":   {"base": 97,   "noise": 1.8,  "drift_per_day": [-0.11, -0.19, -0.08, -0.24, -0.13]},
}

print("Generating data...")

rows = []

for asset_idx, asset in enumerate(ASSET_NAMES):
    drift_temp = SENSORS["temperature"]["drift_per_day"][asset_idx]
    drift_vib = SENSORS["vibration"]["drift_per_day"][asset_idx]
    drift_oil = SENSORS["oil_quality"]["drift_per_day"][asset_idx]

    for day in range(DAYS):
        for hour in range(HOURS_PER_DAY):
            timestamp = START_DATE + timedelta(days=day, hours=hour)
            runtime = day * 24 + hour + np.random.normal(0, 1.5)

            temp = SENSORS["temperature"]["base"] + drift_temp * day \
                + np.random.normal(0, SENSORS["temperature"]["noise"])
            temp += np.random.choice([0, np.random.uniform(6, 14)],
                                     p=[0.993, 0.007])

            vib = SENSORS["vibration"]["base"] + drift_vib * day \
                + np.random.normal(0, SENSORS["vibration"]["noise"])
            vib += np.random.choice([0, np.random.uniform(1.2,
                                    3.8)], p=[0.992, 0.008])

            oil = max(25, SENSORS["oil_quality"]["base"] + drift_oil * day
                      + np.random.normal(0, SENSORS["oil_quality"]["noise"]))
            oil -= np.random.choice([0,
                                    np.random.uniform(4, 12)], p=[0.99, 0.01])

            faulty = 1 if (temp > 82 or vib > 4.0 or oil < 65) else 0

            rows.append({
                "asset_id": asset,
                "timestamp": timestamp,
                "temperature_C": round(temp, 2),
                "vibration_mm_s": round(vib, 3),
                "oil_quality_index": round(oil, 1),
                "runtime_hours": round(runtime, 1),
                "is_anomaly": faulty
            })

df = pd.DataFrame(rows)

print(
    f"Created {len(df)} rows ({len(ASSET_NAMES)} assets × {DAYS} days × 24 hours)")
print(df["asset_id"].value_counts())

df.to_csv("data/raw_sensor_data.csv", index=False)
print("Saved → data/raw_sensor_data.csv")
