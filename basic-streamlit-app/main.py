'''
Welcome! Before you start, follow these steps to run the app:

1. Open a terminal.
2. Navigate to the project directory where `main.py` is located:
                 cd basic_streamlit_app
3. Run the following command to start the app: 
                streamlit run main.py


Once the command runs, the app will open automatically in your web browser.

'''

import streamlit as st
import pandas as pd

st.title("Palmer's Penguins Interactive App")
st.write("Explore the Palmer's Penguins dataset with interactive filters! Discover details about each penguin, from its species to its island habitat, and dive into the data with ease")

st.write("Below is the complete dataset loaded from a CSV File:")
df = pd.read_csv("data/penguins.csv")
st.dataframe(df)

df["sex"] = df["sex"].fillna("")

island = st.radio("Select an Island:",list(df["island"].unique()))
gender = st.selectbox("Select Gender:", [ "male", "female"])
year_range = st.slider(
    "Select Year Range",
    min_value=int(df["year"].min()), 
    max_value=int(df["year"].max()), 
    value=(int(df["year"].min()), int(df["year"].max())))



filtered_df = df[
    (df["island"] == island) &
    (df["sex"] == gender) &
    (df["year"] >= year_range[0]) & (df["year"] <= year_range[1]) 
    
]

st.write(filtered_df)


