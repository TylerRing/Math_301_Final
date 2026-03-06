import requests
import pandas as pd
import time
import os




NASS_API_KEY = os.getenv("NASS_API_KEY")
NOAA_TOKEN = os.getenv("NOAA_TOKEN")



# Corn Yield 

def get_nebraska_corn_yield():

    url = "https://quickstats.nass.usda.gov/api/api_GET/"

    params = {
        "key": NASS_API_KEY,
        "commodity_desc": "CORN",
        "statisticcat_desc": "YIELD",
        "unit_desc": "BU / ACRE",
        "state_name": "NEBRASKA",
        "agg_level_desc": "STATE",   
        "year__GE": "2000",
        "format": "JSON"
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()
    df = pd.DataFrame(data["data"])

    df = df[['year', 'Value']]
    df['year'] = pd.to_numeric(df['year'], errors='coerce')
    df['Value'] = df['Value'].str.replace(',', '', regex=False)
    df['Value'] = pd.to_numeric(df['Value'], errors='coerce')

    df = df.dropna(subset=['year', 'Value'])
    df = df.rename(columns={'Value': 'yield_bu_per_acre'})
    df = df.drop_duplicates(subset=['year'])
    df = df.sort_values('year')

    print("\nCorn yield data sample:")
    print(df.head())

    return df



# Precipitation 
def get_nebraska_precipitation():

    import time
    import requests

    url = "https://www.ncdc.noaa.gov/cdo-web/api/v2/data"
    headers = {"token": NOAA_TOKEN}

    station_id = "GHCND:USW00014939"  # Lincoln Airport

    all_data = []

    for year in range(2000, 2024):

        offset = 1

        while True:

            params = {
                "datasetid": "GHCND",
                "datatypeid": "PRCP",
                "stationid": station_id,
                "startdate": f"{year}-01-01",
                "enddate": f"{year}-12-31",
                "units": "standard",
                "limit": 1000,
                "offset": offset
            }

            
            for attempt in range(5):
                try:
                    response = requests.get(url, headers=headers, params=params, timeout=30)
                    response.raise_for_status()
                    break
                except requests.exceptions.HTTPError as e:
                    if response.status_code == 503:
                        print(f"503 error for {year}. Waiting before retry...")
                        time.sleep(5)
                    else:
                        raise e
                except requests.exceptions.RequestException:
                    print("Network issue. Retrying...")
                    time.sleep(5)
            else:
                print(f"Failed permanently for {year}. Skipping year.")
                break
            

            results = response.json().get("results", [])

            if not results:
                break

            all_data.extend(results)

            offset += 1000
            time.sleep(1)   # slower request kept getting errors

        print(f"{year} complete")

    df = pd.DataFrame(all_data)

    df['date'] = pd.to_datetime(df['date'])
    df['value'] = pd.to_numeric(df['value'], errors='coerce')
    df = df.dropna(subset=['value'])

    df['year'] = df['date'].dt.year

    annual_precip = df.groupby('year')['value'].sum().reset_index()
    annual_precip = annual_precip.rename(columns={'value': 'annual_precip_in'})

    print("\nAnnual precipitation sample:")
    print(annual_precip.head())

    return annual_precip

# Join Datasets

def join_datasets(corn_df, precip_df):

    merged = pd.merge(corn_df, precip_df, on='year', how='inner')

    print("\nMerged dataset sample:")
    print(merged.head())

    return merged



# Main had to remove graphs for github

if __name__ == "__main__":

    corn_df = get_nebraska_corn_yield()
    precip_df = get_nebraska_precipitation()
    merged_df = join_datasets(corn_df, precip_df)

    # Save dataset
    os.makedirs("output", exist_ok=True)
    merged_df.to_csv("output/nebraska_corn_weather.csv", index=False)

    # Correlation
    correlation = merged_df['annual_precip_in'].corr(
                  merged_df['yield_bu_per_acre'])
    print("Correlation:", correlation)

    # Regression
    import statsmodels.api as sm

    X = sm.add_constant(merged_df['annual_precip_in'])
    y = merged_df['yield_bu_per_acre']

    model = sm.OLS(y, X).fit()
    print(model.summary())

    # Fail if output is invalid (important for CI)
    if merged_df.empty:
        raise ValueError("Merged dataset is empty")