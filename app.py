import pandas as pd
import streamlit as st
import joblib


# Load the model
model, prob_threshold = joblib.load('./models/rf_model2_with_threshold.joblib')

# Load the data
@st.cache_data
def load_data():
    df = pd.read_csv('./data/data_less_features_no_label.csv')
    return df

df = load_data()

# Title
st.title('Conversion Prediction')

# Input fields
country = st.selectbox('Country', df['country'].unique())
productgroup = st.selectbox('Product Group', df['productgroup'].unique())
category = st.selectbox('Category', df[df['productgroup'] == productgroup]['category'].unique())
gender = st.selectbox('Gender', df[df['category'] == category]['gender'].unique())
month = st.selectbox('Month', df['month'].unique())
ratio = st.slider('Ratio', min_value = 0.3, max_value = 1.0, step = 0.01)
promo1 = st.selectbox('Promo1', df['promo1'].unique())
promo2 = st.selectbox('Promo2', df['promo2'].unique())

# Create a new dataframe with the input values
new_data = pd.DataFrame({
    'country': [country],
    'productgroup': [productgroup],
    'category': [category],
    'gender': [gender],
    'month': [month],
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
