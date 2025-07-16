import streamlit as st
import pandas as pd
import joblib

# 🎉 Load the trained model
model = joblib.load('house_price_model.pkl')

# 🖥️ Title
st.title("🏠 House Price Prediction App")

# 🧮 Get input from the user
bedrooms = st.number_input("Bedrooms", min_value=0)
bathrooms = st.number_input("Bathrooms", min_value=0.0)
sqft_living = st.number_input("Living Area (sqft)", min_value=0)
sqft_lot = st.number_input("Lot Area (sqft)", min_value=0)
floors = st.number_input("Floors", min_value=0.0)
waterfront = st.selectbox("Waterfront View?", [0, 1])
view = st.number_input("View", min_value=0)
condition = st.number_input("Condition", min_value=1, max_value=5)
sqft_above = st.number_input("Sqft Above", min_value=0)
sqft_basement = st.number_input("Sqft Basement", min_value=0)
yr_built = st.number_input("Year Built", min_value=1800, max_value=2025)
yr_renovated = st.number_input("Year Renovated", min_value=0, max_value=2025)

# 📦 Predict when button clicked
if st.button("Predict Price"):
    input_data = pd.DataFrame([[bedrooms, bathrooms, sqft_living, sqft_lot, floors,
                                waterfront, view, condition, sqft_above, sqft_basement,
                                yr_built, yr_renovated]],
                              columns=['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors',
                                       'waterfront', 'view', 'condition', 'sqft_above', 'sqft_basement',
                                       'yr_built', 'yr_renovated'])
    
    prediction = model.predict(input_data)
    st.success(f"💰 Estimated Price: ${prediction[0]:,.2f}")
