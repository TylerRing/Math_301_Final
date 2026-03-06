import streamlit as st
import pandas as pd
import plotly.express as px

REQUIRED_COLUMNS = {"year", "yield_bu_per_acre", "annual_precip_in"}

# Title of the app
st.title("Corn Weather Analysis")

# Load dataset
@st.cache_data
def load_data():
    data = pd.read_csv("../data/corn_weather_clean.csv")
    return data

# Load the data
data = load_data()

# Validate required columns
missing = REQUIRED_COLUMNS - set(data.columns)
if missing:
    st.error(f"Dataset is missing required columns: {missing}")
    st.stop()

# Display a sample of the dataset
st.write("Sample Data:")
st.write(data.head())

# Create a Plotly chart
fig = px.line(data, x='year', y='yield_bu_per_acre', title='Corn Yield Over Time')
st.plotly_chart(fig)

# Scatter: precipitation vs yield
fig2 = px.scatter(data, x='annual_precip_in', y='yield_bu_per_acre',
                  title='Annual Precipitation vs Corn Yield',
                  labels={'annual_precip_in': 'Annual Precipitation (in)',
                          'yield_bu_per_acre': 'Yield (bu/acre)'})
st.plotly_chart(fig2)
