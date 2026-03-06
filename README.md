# Math_301_Final
# Corn Yield and Weather Analysis

This project analyzes the relationship between weather variables and corn yield in the United States.

## Data Pipeline

The pipeline automatically downloads weather and yield data, cleans the datasets, and produces a merged dataset used by the web application.

The pipeline script is located in:

pipeline/pipeline.py

The cleaned dataset is saved to:

data/corn_weather_clean.csv

## Running the Application

Clone the repository:

git clone <repo-url>

Install dependencies:

pip install -r requirements.txt

Run the Streamlit app:

streamlit run app/app.py
