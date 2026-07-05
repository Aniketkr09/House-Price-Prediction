import os
import joblib
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor

# ------------------------
# Load Dataset
# ------------------------

df = pd.read_csv("data/housing.csv")

# Features
X = df[[
    "area_sqft",
    "bedrooms",
    "bathrooms",
    "floor",
    "location"
]]

# Target
y = df["price"]

# ------------------------
# Preprocessing
# ------------------------

preprocessor = ColumnTransformer(
    transformers=[
        (
            "location",
            OneHotEncoder(handle_unknown="ignore"),
            ["location"]
        )
    ],
    remainder="passthrough"
)

# ------------------------
# Model
# ------------------------

pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("model", RandomForestRegressor(
        n_estimators=200,
        random_state=42
    ))
])

# ------------------------
# Train Model
# ------------------------

pipeline.fit(X, y)

# ------------------------
# Save Model
# ------------------------

os.makedirs("model", exist_ok=True)

joblib.dump(
    pipeline,
    "model/house_price_model.pkl"
)

print("✅ Model Trained Successfully!")