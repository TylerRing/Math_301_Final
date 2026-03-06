# Fetch Weather Data Script

import requests
import pandas as pd

API_URL = 'https://api.weather.com/'  # Example API URL

def fetch_weather_data(location):
    response = requests.get(f"{API_URL}?location={location}")
    data = response.json()
    return pd.DataFrame(data)

if __name__ == '__main__':
    # Example usage
    location = 'New York'
    weather_data = fetch_weather_data(location)
    print(weather_data)