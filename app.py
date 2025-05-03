'''import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model
model = joblib.load("airbnb_model.pkl")

st.title("Airbnb Price Predictor")

st.markdown("### Enter Listing Details")

# User inputs
latitude = st.number_input("Latitude", value=40.7128)
longitude = st.number_input("Longitude", value=-74.0060)
minimum_nights = st.number_input("Minimum Nights", min_value=1, value=2)
number_of_reviews = st.number_input("Number of Reviews", min_value=0, value=10)
reviews_per_month = st.number_input("Reviews per Month", min_value=0.0, value=0.5)
availability_365 = st.number_input("Availability (days/year)", min_value=0, max_value=365, value=180)
room_type = st.selectbox("Room Type", ["Entire home/apt", "Private room", "Shared room"])

# Encode room_type manually
room_type_entire = 1 if room_type == "Entire home/apt" else 0
room_type_private = 1 if room_type == "Private room" else 0
room_type_shared = 1 if room_type == "Shared room" else 0

# Create input DataFrame (using only the necessary columns)
input_data = pd.DataFrame({
    'latitude': [latitude],
    'longitude': [longitude],
    'minimum_nights': [minimum_nights],
    'number_of_reviews': [number_of_reviews],
    'reviews_per_month': [reviews_per_month],
    'availability_365': [availability_365],
    'room_type_Private room': [room_type_private],
    'room_type_Shared room': [room_type_shared]
})

if st.button("Predict Price"):
    prediction = model.predict(input_data)
    st.success(f"Estimated Price: ${prediction[0]:.2f}")'''
import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("airbnb_model.pkl")

st.title("Airbnb Price Predictor")

st.markdown("### Enter Listing Details")

# User inputs
latitude = st.number_input("Latitude", value=40.7128)
longitude = st.number_input("Longitude", value=-74.0060)
minimum_nights = st.number_input("Minimum Nights", min_value=1, value=2)
number_of_reviews = st.number_input("Number of Reviews", min_value=0, value=10)
reviews_per_month = st.number_input("Reviews per Month", min_value=0.0, value=0.5)
availability_365 = st.number_input("Availability (days/year)", min_value=0, max_value=365, value=180)
room_type = st.selectbox("Room Type", ["Entire home/apt", "Private room"])

# One-hot encode 'Private room' (assuming model was trained with drop_first=True)
room_type_private = 1 if room_type == "Private room" else 0

# Create input DataFrame
input_data = pd.DataFrame({
    'latitude': [latitude],
    'longitude': [longitude],
    'minimum_nights': [minimum_nights],
    'number_of_reviews': [number_of_reviews],
    'reviews_per_month': [reviews_per_month],
    'availability_365': [availability_365],
    'room_type_Private room': [room_type_private]
})

# Predict price
if st.button("Predict Price"):
    try:
        prediction = model.predict(input_data)
        st.success(f"Estimated Price: ${prediction[0]:.2f}")
    except Exception as e:
        st.error(f"Prediction failed: {e}")


