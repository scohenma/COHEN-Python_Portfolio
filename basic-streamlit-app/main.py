
import streamlit as st
import pandas as pd

st.title("Palmer's Penguins Interactive App")
st.write("Explore the Palmer's Penguins dataset with interactive filters! Discover details about each penguin, from its species to its island habitat, and dive into the data with ease")

st.write("Below is the complete dataset loaded from a CSV File:")
df = pd.read_csv("data/penguins.csv")
st.dataframe(df)

island = st.radio("Select an Island:", ["All"] + list(df["island"].unique()))
gender = st.selectbox("Select Gender:", ["All", "Male", "Female"])
species_selected = st.multiselect("Select Species:", df["species"].unique(), default=df["species"].unique())


