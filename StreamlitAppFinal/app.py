import streamlit as st
import pandas as pd

# Load your dataset
df = pd.read_csv("World University Rankings 2023.csv")

# Set page title and intro text
st.set_page_config(page_title="College Compass", layout="wide")
st.title("College Compass")
st.markdown("Welcome! Are you deciding where to go to college? This tool helps you explore and compare top universities based on your goals.")

# Step 1: Ask the user what kind of help they need
user_choice = st.radio("What would you like to do?",
                       ["I already know my options – help me compare them",
                        "I haven’t created a college list yet – help me generate one"])

# If they choose to compare, show Option 1 logic
if user_choice == "I already know my options – help me compare them":
    # (This is where the comparison code goes — copy it right here)
    st.subheader("Compare Universities")

    universities_to_compare = st.multiselect(
        "Select universities to compare:",
        options=df["Name of University"].unique()
    )
    if universities_to_compare:
        comparison_df = df[df["Name of University"].isin(universities_to_compare)]
        st.dataframe(comparison_df.set_index("Name of University"))
    else:
        st.info("Please select at least one university to compare.")

elif user_choice == "I haven’t created a college list yet – help me generate one":
    st.subheader("Build Your College List")

    # Q1: Location preference
    location_pref = st.multiselect(
        "Preferred locations (countries):",
        options=df["Location"].unique()
    )

    # Q2: International student friendliness
    wants_intl = st.selectbox(
        "Are you an international student?",
        ["Yes", "No"]
    )

    # Q3: Desired minimum overall score
    min_score = st.slider(
        "Minimum overall score you're aiming for (0 to 100):",
        min_value=0.0,
        max_value=100.0,
        value=85.0
    )

    # Filter based on answers
    filtered_df = df.copy()

    if location_pref:
        filtered_df = filtered_df[filtered_df["Location"].isin(location_pref)]

    if wants_intl == "Yes":
        # Strip % sign and convert to float
        filtered_df["Intl_Student_Num"] = filtered_df["International Student"].str.replace('%', '').astype(float)
        filtered_df = filtered_df[filtered_df["Intl_Student_Num"] >= 20.0]  # Filter by reasonable threshold

    # Convert OverAll Score to float if not already
    filtered_df["OverAll Score"] = pd.to_numeric(filtered_df["OverAll Score"], errors='coerce')
    filtered_df = filtered_df[filtered_df["OverAll Score"] >= min_score]

    # Sort and display
    filtered_df = filtered_df.sort_values("OverAll Score", ascending=False)

    if not filtered_df.empty:
        st.success(f"{len(filtered_df)} universities match your preferences.")
        st.dataframe(filtered_df[[
            "Name of University", "Location", "International Student", "OverAll Score"
        ]].reset_index(drop=True))
    else:
        st.warning("No universities match your criteria. Try adjusting your preferences.")
