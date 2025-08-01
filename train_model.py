import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor
import joblib

# Load your preprocessed data
df = pd.read_csv("preprocessed_ev_data.csv")

# Select the correct feature columns
features = [
    'months_since_start',
    'county_encoded',
    'ev_total_lag1',
    'ev_total_lag2',
    'ev_total_lag3',
    'ev_total_roll_mean_3',
    'ev_total_pct_change_1',
    'ev_total_pct_change_3',
    'ev_growth_slope'
]

# Target variable
target = 'Electric Vehicle (EV) Total'

# Drop rows with missing values in features or target
df = df.dropna(subset=features + [target])

# Split into X (inputs) and y (output)
X = df[features]
y = df[target]

# Train a model
model = DecisionTreeRegressor()
model.fit(X, y)

# Save the model
joblib.dump(model, 'forecasting_ev_model.pkl')

print("✅ Model trained and saved as forecasting_ev_model.pkl")