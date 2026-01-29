# My ML Project 2026

This is my first full-stack machine learning project as a beginner.

Tech stack (planned):
- Frontend: React (with Vite)
- Backend: Python + FastAPI
- Data: CSV files
- ML: scikit-learn

Setup in progress – Day 1
## Data (Day 2)

### Raw Sensor Data
- **File**: `data/raw_sensor_data.csv`
- **Rows**: 10,800
- **Structure**: 5 industrial assets × 90 days × 24 hours (hourly readings)
- **Columns**:
  - `asset_id`              : Machine name (e.g. Gearbox_1, Compressor_A, Pump_B, Turbine_X, Motor_5)
  - `timestamp`             : Date + hour of measurement
  - `temperature_C`         : Temperature (°C)
  - `vibration_mm_s`        : Vibration velocity (mm/s)
  - `oil_quality_index`     : Oil condition score (higher = cleaner/better)
  - `runtime_hours`         : Cumulative operating hours
  - `is_anomaly`            : Rule-based flag (1 = potential fault detected)

**How it was created**:
- Synthetic data generated with `generate_data.py`
- Includes gradual degradation over time (different rate per asset)
- Random noise + occasional realistic spikes/drops (to simulate faults)