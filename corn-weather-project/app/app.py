import streamlit as st
import pandas as pd

# Sample weather data
weather_data = {
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03'],
    'Temperature (°C)': [20, 21, 19],
    'Humidity (%)': [30, 35, 33]
}

df = pd.DataFrame(weather_data)

st.title('Weather Dashboard')

# Display temperature trends
st.line_chart(df[['Date', 'Temperature (°C)']].set_index('Date'))

# Display humidity metrics
st.line_chart(df[['Date', 'Humidity (%)']].set_index('Date'))

# Display data table
download = st.download_button(
    label='Download data as CSV',
    data=df.to_csv(index=False),
    file_name='weather_data.csv',
    mime='text/csv'
)

st.dataframe(df)