import plotly.express as px
import pandas as pd
import streamlit as st

#config AppWeb layout

st.set_page_config(layout="wide")

#loading files to read
df = pd.read_csv("D:\EricHDD\Projects\dashboards_project\supermarket_sales.csv", sep=";", decimal=",")

#converting "date" to library understand and organize
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))

month = st.sidebar.selectbox("Month", df["Month"].unique())

filter = df[df["Month"] == month]
