import streamlit as st
import pandas as pd

# Page config
st.set_page_config(page_title="Netflix Data Insights", layout="wide")
# Title
st.title("🎬 Netflix Data Insights")
# Load data
df = pd.read_csv("data/sample_output.csv")
# Clean column names
df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace("_", " ").str.title()
# Top metric
st.metric("Top Movie", df.iloc[0]["Movie Title"])
# Table section
st.subheader("📊 Top Rated Movies")
st.dataframe(df, use_container_width=True)
# Chart section
st.subheader("📈 Average Ratings (Top 10)")

chart_data = df.head(10).set_index("Movie Title")["Average Rating"]
st.bar_chart(chart_data)