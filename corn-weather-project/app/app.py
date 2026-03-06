import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Corn Yield and Weather Analysis")

df = pd.read_csv("../data/corn_weather_clean.csv")

st.write(df)

state = st.selectbox("Select State", df["State"].unique())

filtered = df[df["State"] == state]

fig, ax = plt.subplots()
ax.scatter(filtered["Avg_Temp"], filtered["Corn_Yield"])

st.pyplot(fig)
