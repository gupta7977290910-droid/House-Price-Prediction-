import streamlit as st
import joblib
import numpy as np

st.title("House Price Predictor App")
model=joblib.load("house_model.pkl")
scale=joblib.load("scale.pkl")

st.header("Enter House Details To Predict The Current Price")

area=st.number_input("Enter The Area in SQFT",min_value=1)
bedrooms=st.number_input("Enter The Number of Bedrooms",min_value=0)
bathrooms=st.number_input("Enter The Number of Bathrooms",min_value=0)
stories=st.number_input("Enter The Floor",min_value=0)
mainroad=st.number_input("MainRoad (Yes/No)",min_value=0)
guestroom=st.number_input("Guestroom(Yes/No)",min_value=0)
basement=st.number_input("Basement(Yes/No)",min_value=0)
hotwaterheating=st.number_input("Water Heating Facility(Yes/No)",min_value=0)
airconditioning=st.number_input("Air Conditioning(Yes/No)",min_value=0)
parking=st.number_input("Parking(Yes/No)",min_value=0)
prefarea=st.number_input("Preferrable Area(Yes/No)",min_value=0)
furnishingstatus_semi_furnished=st.number_input("furnishingstatus_semi-furnished(Yes/No)",min_value=0)
furnishingstatus_unfurnished=st.number_input("furnishingstatus_unfurnished(Yes/No)",min_value=0)






if st.button("Predict Price"):
    input_data = np.array([[area, bedrooms, bathrooms,stories,mainroad,guestroom,basement,hotwaterheating,airconditioning,parking,prefarea,furnishingstatus_semi_furnished,furnishingstatus_unfurnished]])
   
    # Apply scaling before prediction
    input_scaled = scaler.transform(input_data)
   
    prediction = model.predict(input_scaled)
   
    st.success(f"Predicted Price: {prediction[0]}")
