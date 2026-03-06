import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load weather data
@st.cache_data
def load_data():
    # Placeholder for actual weather data loading logic
    # For example, you can load a CSV or call an API to fetch weather data
    # Here, we're creating a sample DataFrame
    data = {
        'Date': pd.date_range(start='2022-01-01', periods=100),
        'Temperature': pd.np.random.randint(0, 100, size=100),
        'Humidity': pd.np.random.randint(20, 80, size=100)
    }
    return pd.DataFrame(data)


# Streamlit app layout
st.title('Weather Data Visualization')

# Load the data
weather_data = load_data()

# Sidebar for filters
st.sidebar.header('Filters')
selected_date = st.sidebar.date_input('Select Date', value=pd.to_datetime('2022-01-01'), min_value=weather_data['Date'].min(), max_value=weather_data['Date'].max())

# Filter data based on user input
filtered_data = weather_data[weather_data['Date'] == pd.to_datetime(selected_date)]

# Display filtered data
st.write(filtered_data)

# Plotting
st.subheader('Temperature and Humidity')
fig, ax = plt.subplots()
ax.plot(filtered_data['Date'], filtered_data['Temperature'], label='Temperature', color='r')
ax.plot(filtered_data['Date'], filtered_data['Humidity'], label='Humidity', color='b')
ax.set_xlabel('Date')
ax.set_ylabel('Value')
ax.legend()

# Show the plot in Streamlit
st.pyplot(fig)