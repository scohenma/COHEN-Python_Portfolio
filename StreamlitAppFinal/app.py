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
        options=df["Name of University"].unique() )
    if universities_to_compare:
        comparison_df = df[df["Name of University"].isin(universities_to_compare)]
        st.dataframe(comparison_df.set_index("Name of University"))
    else:
        st.info("Please select at least one university to compare.")

elif user_choice == "I haven’t created a college list yet – help me generate one":
    st.subheader("Build Your College List")

   # Option 2 UI
st.subheader("🎯 Option 2: Help Me Build My College List")

with st.form("college_form"):
    st.write("Fill out your preferences to discover universities that match your profile.")

    # 1. International student radio
    is_international = st.radio("Are you an international student?", ("Yes", "No"))

    # 2. Clean Location column before sorting to prevent type error
    cleaned_locations = df["Location"].dropna().astype(str).unique()
    location_pref = st.selectbox("Preferred location", options=["Any"] + sorted(cleaned_locations))

    # 3. Sliders for preferences
    max_students_per_staff = st.slider("Max students per staff", 5.0, 30.0, 15.0)
    min_score = st.slider("Minimum overall score", 0.0, 100.0, 60.0)

    # 4. Priority metric
    priority_metric = st.selectbox("What's more important to you?", ("Teaching Score", "Research Score"))

    # 5. Submit button inside form
    submitted = st.form_submit_button("Find universities")

if submitted:
    results = df.copy()
    # Apply filters
    if is_international == "Yes":
        results = results[results["International Student"] > 20]

    if location_pref != "Any":
        results = results[results["Location"] == location_pref]

    results = results[
        (results["No of student per staff"] <= max_students_per_staff) &
        (results["OverAll Score"] >= min_score) ]
    
    results = results.sort_values(by=priority_metric, ascending=False)

    st.write(f"Found {len(results)} universities that match your filters:")
    st.dataframe(results[[
        "Name of University", "Location", "OverAll Score",
        "No of student per staff", "International Student",
        "Teaching Score", "Research Score"
    ]].reset_index(drop=True))