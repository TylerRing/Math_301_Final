import requests
import pandas as pd
import os

NOAA_TOKEN = os.getenv("NOAA_TOKEN")
API_URL = "https://www.ncdc.noaa.gov/cdo-web/api/v2/data"

REQUIRED_COLUMNS = {"year", "yield_bu_per_acre", "annual_precip_in"}


def fetch_weather_data(station_id, start_date, end_date, datatype="PRCP"):
    """Fetch weather data from the NOAA CDO API."""
    if not NOAA_TOKEN:
        raise ValueError(
            "NOAA_TOKEN environment variable is not set. "
            "Set it to your NOAA CDO API token before running this script."
        )
    headers = {"token": NOAA_TOKEN}
    params = {
        "datasetid": "GHCND",
        "datatypeid": datatype,
        "stationid": station_id,
        "startdate": start_date,
        "enddate": end_date,
        "units": "standard",
        "limit": 1000,
    }
    try:
        response = requests.get(API_URL, headers=headers, params=params, timeout=30)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        raise requests.exceptions.HTTPError(
            f"NOAA API request failed with status {response.status_code}. "
            "Check that NOAA_TOKEN is valid and that the request parameters are correct."
        ) from e
    results = response.json().get("results", [])
    return pd.DataFrame(results)


if __name__ == "__main__":
    # Example: Lincoln Airport station, full year 2023
    station_id = "GHCND:USW00014939"
    df = fetch_weather_data(station_id, "2023-01-01", "2023-12-31")
    print(df.head())
