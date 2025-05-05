import streamlit as st
import pandas as pd

# Load your dataset
df = pd.read_csv("World University Rankings 2023.csv")

# Preprocess for numeric fields
df["No of student per staff"] = pd.to_numeric(df["No of student per staff"], errors="coerce")
df["OverAll Score"] = pd.to_numeric(df["OverAll Score"], errors="coerce")
df["Teaching Score"] = pd.to_numeric(df["Teaching Score"], errors="coerce")
df["Research Score"] = pd.to_numeric(df["Research Score"], errors="coerce")
df["International Student"] = df["International Student"].str.replace('%', '').astype(float)

# App title
st.title("🎓 College Compass: Your Personalized University Advisor")

# Ask user what they want to do
option = st.radio(
    "What would you like to do?",
    ["🎯 Option 1: Compare Universities", "🎯 Option 2: Help Me Build My College List"]
)

# --------------------------------
# 🎯 Option 1: Compare Universities
# --------------------------------
if option == "🎯 Option 1: Compare Universities":
    st.subheader("🔍 Compare Universities Side-by-Side")
    
    universities = df["Name of University"].dropna().sort_values().unique()
    
    col1, col2 = st.columns(2)
    with col1:
        uni1 = st.selectbox("Select first university:", universities, key="uni1")
    with col2:
        uni2 = st.selectbox("Select second university:", universities, key="uni2")
    
    if uni1 and uni2:
        selected = df[df["Name of University"].isin([uni1, uni2])]
        st.write("📊 Here's how they compare:")
        st.dataframe(selected.set_index("Name of University").T)

# -----------------------------------------------
# 🎯 Option 2: Build a Custom College Recommendation
# -----------------------------------------------
elif option == "🎯 Option 2: Help Me Build My College List":
    st.subheader("🎯 Help Me Build My College List")

    with st.form("college_form"):
        st.write("Fill out your preferences to discover universities that match your profile.")

        # Question 1: International student
        is_international = st.radio("Are you an international student?", ("Yes", "No"))

        # Question 2: Location preference
        locations = df["Location"].dropna().astype(str).unique()
        location_pref = st.selectbox("Preferred location", options=["Any"] + sorted(locations))

        # Question 3: Student/staff ratio
        max_students_per_staff = st.slider("Max number of students per staff", 5.0, 30.0, 15.0)

        # Question 4: Minimum Overall Score
        min_score = st.slider("Minimum Overall Score", 0.0, 100.0, 60.0)

        # Question 5: Priority metric
        priority = st.selectbox("What's more important to you?", ["Teaching Score", "Research Score"])

        # Submit button
        submitted = st.form_submit_button("🎓 Find My Universities")

    if submitted:
        filtered = df.copy()

        if location_pref != "Any":
            filtered = filtered[filtered["Location"] == location_pref]

        if is_international == "Yes":
            filtered = filtered[filtered["International Student"] >= 30.0]

        filtered = filtered[filtered["No of student per staff"] <= max_students_per_staff]
        filtered = filtered[filtered["OverAll Score"] >= min_score]

        filtered = filtered.sort_values(by=priority, ascending=False)

        if not filtered.empty:
            st.success(f"✅ Found {len(filtered)} universities matching your profile.")
            st.dataframe(filtered.reset_index(drop=True))
        else:
            st.warning("No universities matched all your criteria. Try adjusting your filters.")
