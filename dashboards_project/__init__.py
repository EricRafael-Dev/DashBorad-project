import plotly.express as px
import pandas as pd
import streamlit as st

#config AppWeb layout

st.set_page_config(layout="wide")

#loading files to read
df = pd.read_csv("D:\EricHDD\Projects\dashboards_project\supermarket_sales.csv", sep=";", decimal=",")
df