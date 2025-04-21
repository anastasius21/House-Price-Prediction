import streamlit as st
import pandas as pd
import numpy as np
import pickle

model = pickle.load(open('model.pkl','rb'))

ocean_proximity_options = ['<1H OCEAN','NEAR BAY','INLAND','ISLAND','NEAR OCEAN']

st.title('House Price Prediction App')

st.header('Fill in the details below to get the price prediction')


longitude = st.number_input('Longitude:')
latitude = st.number_input('Latitude:')
housing_median_age = st.slider('Housing Median Age:',1,100,30)
total_rooms = st.number_input('Total Rooms:')
total_bedrooms = st.number_input('Total Bedrooms:')
population = st.number_input('Population:')
households = st.number_input('Households:')
median_income = st.number_input('Median Income:')
op = st.selectbox('Ocean Proximity',ocean_proximity_options)



if st.button('Predict'):
    total_rooms = np.log(total_rooms + 1)
    total_bedrooms = np.log(total_bedrooms + 1)
    population = np.log(population + 1)
    households = np.log(households + 1)
    bedrooms_ratio = total_bedrooms/total_rooms
    households_rooms = total_rooms/households
    ocean_prox_encoded = [1 if op == label else 0 for label in ocean_proximity_options]
    input_data=[
        longitude,
        latitude,
        housing_median_age,
        total_rooms,
        total_bedrooms,
        population,
        households,
        median_income,
        bedrooms_ratio,
        households_rooms
    ] + ocean_prox_encoded
    df = pd.DataFrame([input_data])
    prediction = model.predict(df)[0]
    st.success(f'The Median Housing Price is predicted to be: {prediction}')

