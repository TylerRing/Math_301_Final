import pandas as pd

def clean_weather_data(data):
    # Remove duplicates
    data = data.drop_duplicates()
    
    # Fill missing values
    data = data.fillna(method='ffill')
    
    # Convert dates
    data['date'] = pd.to_datetime(data['date'])
    
    # Save processed data to data/processed/
    processed_path = 'data/processed/cleaned_weather_data.csv'
    data.to_csv(processed_path, index=False)
    return processed_path
