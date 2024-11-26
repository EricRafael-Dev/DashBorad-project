import plotly.express as px
import pandas as pd
import streamlit as st
import nbformat

#config AppWeb layout

st.set_page_config(layout="wide")

#loading files to read
df = pd.read_csv("/supermarket_sales.csv", sep=";", decimal=",")

#converting "date" to library understand and organize
df["Date"] = pd.to_datetime(df["Date"])
df["Quantity"] = pd.to_numeric(df["Quantity"])

df = df.sort_values("Date")

df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))

month = st.sidebar.selectbox("Month", df["Month"].unique())


#filtering data per month for time range graphs
filter = df[df["Month"] == month]

#create graps
fig_billing = px.bar(filter, x='Date', y='Total', color="City", title="Billing per year")

city_total = filter.groupby("City")["Total"].sum().reset_index() #grouping Cities with summing the total
fig_cities = px.bar(city_total, x='City', y='Total', title="Billing per city")

fig_payments = px.pie(filter, values="Total", names="Payment", title="Payment Forms")

rating_mean = filter.groupby("City")["Rating"].mean().reset_index() #calculing mean ranting and grouping with cities
fig_rating = px.bar(rating_mean, y='Rating', x='City', title="Rating per city")


#showing graps
fig_billing
fig_cities
fig_payments
fig_rating