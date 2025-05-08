
import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv('universities_cleaned.csv')

st.title("University Comparison Tool")

st.markdown("""
### 🎓 Welcome to the University Finder App!

First of all, **congratulations** 🎉 — if you're exploring any of these universities, it means you're driven, passionate, and thinking deeply about your future. This app is designed to help you make one of the most exciting decisions of your life.

Whether you're trying to figure out *where to apply*, or you're *narrowing down your top choices*, this app will help you explore real data from values-based, high-impact universities across the U.S.
""")

st.sidebar.header("Choose Your Path 🧭")
mode = st.sidebar.radio(
    "What would you like to do?",
    ["Help Me Decide Where to Apply", "Compare My Top 3 Universities"]
)

# Sidebar for user input
st.sidebar.header("Filter Options")
selected_type = st.sidebar.multiselect("Select University Type", options=df['Type'].unique())
selected_athletics = st.sidebar.multiselect("Select Athletics Conference", options=df['Athletics'].unique())

# Filter data based on user input
filtered_df = df
if selected_type:
    filtered_df = filtered_df[filtered_df['Type'].isin(selected_type)]
if selected_athletics:
    filtered_df = filtered_df[filtered_df['Athletics'].isin(selected_athletics)]

# Display filtered data
st.dataframe(filtered_df)