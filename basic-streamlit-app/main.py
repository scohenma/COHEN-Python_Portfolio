
import streamlit as st
import pandas as pd

st.title("Palmer's Penguins Interactive App")
st.write("Explore the Palmer's Penguins dataset with interactive filters! Discover details about each penguin, from its species to its island habitat, and dive into the data with ease")

df = pd.read_csv("data/penguins.csv")
st.write(df)


