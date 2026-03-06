import pandas as pd


def clean_weather_data(file_path):
    """Load, clean, and return weather data from a CSV file."""
    data = pd.read_csv(file_path)

    # Drop rows with missing values
    data.dropna(inplace=True)

    # Convert date column to datetime if present
    if "date" in data.columns:
        data["date"] = pd.to_datetime(data["date"])

    # Remove duplicates
    data.drop_duplicates(inplace=True)

    return data


if __name__ == "__main__":
    # Usage example
    # cleaned_data = clean_weather_data("output/nebraska_corn_weather.csv")
    pass
