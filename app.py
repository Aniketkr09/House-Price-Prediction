import streamlit as st
import pickle
import numpy as np

# Load model
with open("house_model.pkl", "rb") as file:
    model = pickle.load(file)

# App title
st.title("🏠 House Price Prediction")

st.write(
    "Enter house details below to estimate the price."
)

# User inputs (No upper limit)
area = st.number_input(
    "Area (sq. ft.)",
    min_value=500,
    value=5000
)

bedrooms = st.number_input(
    "Bedrooms",
    min_value=1,
    value=3
)

bathrooms = st.number_input(
    "Bathrooms",
    min_value=1,
    value=2
)

parking = st.number_input(
    "Parking Spaces",
    min_value=0,
    value=2
)

# Prediction button
if st.button("Predict Price"):

    input_data = np.array(
        [[area, bedrooms, bathrooms, parking]]
    )

    prediction = model.predict(input_data)

    st.success(
        f"🏠 Estimated House Price: ₹ {prediction[0]:,.0f}"
    )