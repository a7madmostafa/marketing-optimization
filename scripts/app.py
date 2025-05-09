import pandas as pd
import streamlit as st
import joblib


# Load the model
model, prob_threshold = joblib.load('./models/rf_model_with_threshold.joblib')

# Load the data
@st.cache_data
def load_data():
    df = pd.read_csv('../data/data_outliers_cap_features_select.csv')
    return df

df = load_data()

# Title
st.title('Conversion Prediction')

# Input fields
country = st.selectbox('Country', df['country'].unique())
category = st.selectbox('Category', df['category'].unique())
year = st.selectbox('Year', df['year'].unique())
month = st.selectbox('Month', df['month'].unique())
week_number = st.selectbox('Week Number', df['week_number'].unique())
current_price = st.number_input('Current Price')
ratio = st.number_input('Ratio')
promo1 = st.selectbox('Promo1', df['promo1'].unique())
promo2 = st.selectbox('Promo2', df['promo2'].unique())

# Create a new dataframe with the input values
new_data = pd.DataFrame({
    'country': [country],
    'category': [category],
    'year': [year],
    'month': [month],
    'week_number': [week_number],
    'current_price': [current_price],
    'ratio': [ratio],
    'promo1': [promo1],
    'promo2': [promo2]
})

# Prediction button
if st.button('Predict'):

    # Make the prediction
    prediction = model.predict_proba(new_data)[:,1] >= prob_threshold

    # Display the prediction
    if prediction:
        prediction = 'Conversion'
    else:
        prediction = 'No Conversion'

    st.write(prediction)
