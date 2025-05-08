pip install streamlit

import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv('universities_2.csv')

st.title("University Comparison Tool")

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