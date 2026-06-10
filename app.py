import streamlit as st
import pickle
import numpy as np
# Load model
model = pickle.load(open('model.pkl', 'rb'))

st.title("🏠 House Price Prediction App")

st.write("Enter details below:")

# Inputs
area = st.number_input("Area (sq ft)", min_value=500, max_value=5000)
bedrooms = st.slider("Bedrooms", 1, 5)
bathrooms = st.slider("Bathrooms", 1, 4)

# Predict button
if st.button("Predict Price"):
    input_data = np.array([[area, bedrooms, bathrooms]])
    prediction = model.predict(input_data)

    st.success(f"Estimated Price: ₹ {prediction[0]:,.2f}")