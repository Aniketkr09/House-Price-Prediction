from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# ------------------------
# Load Model
# ------------------------

model = joblib.load("model/house_price_model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    area = float(request.form["area_sqft"])
    bedrooms = int(request.form["bedrooms"])
    bathrooms = int(request.form["bathrooms"])
    floor = int(request.form["floor"])
    location = request.form["location"]

    input_data = pd.DataFrame({
        "area_sqft": [area],
        "bedrooms": [bedrooms],
        "bathrooms": [bathrooms],
        "floor": [floor],
        "location": [location]
    })

    prediction = model.predict(input_data)[0]

    prediction = f"₹ {prediction:,.0f}"

    return render_template(
        "index.html",
        prediction=prediction
    )


if __name__ == "__main__":
    app.run(debug=True)
