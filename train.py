import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Load dataset
df = pd.read_csv("Housing.csv")

print("Dataset Preview:")
print(df.head())

# Select features
X = df[['area', 'bedrooms', 'bathrooms', 'parking']]

# Target variable
y = df['price']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Evaluation
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("\nModel Performance")
print("-----------------")
print("Mean Absolute Error:", mae)
print("R² Score:", r2)

# Save model
with open("house_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("\nModel saved as house_model.pkl")