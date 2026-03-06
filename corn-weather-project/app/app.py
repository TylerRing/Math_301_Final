import plotly.express as px

# Demo data
import pandas as pd

demo_data = {
    'date': ['2021-01-01', '2021-02-01', '2021-03-01'],
    'temperature': [21, 22, 23],
    'humidity': [30, 35, 40]
}
df = pd.DataFrame(demo_data)

# Your Plotly code to visualize data here, using df
print(df)