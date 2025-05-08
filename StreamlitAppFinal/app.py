import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("universities_final_cleaned.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Ensure columns are correct
df.columns = [
    "University", "Rank", "Location", "Undergrad Enrollment", "Tuition",
    "International Students (%)", "Student-Faculty Ratio", "Athletics", "Mission", "Type"
]

# Convert numerical fields
df["International_clean"] = df["International Students (%)"].astype(float)
df["Ratio_clean"] = df["Student-Faculty Ratio"].astype(float)
df["Tuition_clean"] = df["Tuition"].astype(float)

# -----------------------------------------------------------
# 🎓 App Title and Introduction
# -----------------------------------------------------------

st.title("University Comparison Tool")

st.markdown("""
### 🎓 Welcome to the University Explorer App

As a Notre Dame student, I’ve often heard people say: _"There’s just something about this place."_ That *something* — values, community, purpose, spirit — inspired me to build this tool.

This app helps students explore universities that share that same heart: schools where excellence meets mission, and success is about more than just rankings.

---

#### 🌟 Featured Universities
""")

# Creative listing of universities
featured_universities = [
    "🏰 University of Notre Dame",
    "📚 Georgetown University",
    "🦅 Boston College",
    "🐾 Villanova University",
    "🤘 University of Texas at Austin",
    "🔵 Duke University",
    "🌴 Santa Clara University",
    "💙 Saint Louis University",
    "🧠 University of Virginia",
    "🧡 Syracuse University"
]

for uni in featured_universities:
    st.markdown(f"- {uni}")

# -----------------------------------------------------------
# 🧭 User Option: Decide or Compare
# -----------------------------------------------------------

st.markdown("### 🔍 What would you like to do?")
mode = st.radio(
    "Choose one:",
    ["Help Me Decide Where to Apply", "Compare My Top 3 Universities"]
)

# -----------------------------------------------------------
# 🎯 HELP ME DECIDE SECTION
# -----------------------------------------------------------

if mode == "Help Me Decide Where to Apply":
    st.markdown("## 🎯 Let’s Find Your Fit")
    st.write("Use the filters below to narrow down the schools that match your goals:")

    col1, col2 = st.columns(2)

    with col1:
        type_filter = st.selectbox("Select University Type", ["All", "Public", "Private"])
        tuition_max = st.slider("Max Tuition ($)", min_value=40000, max_value=70000, value=65000)

    with col2:
        intl_filter = st.slider("Minimum % of International Students", 0.0, 20.0, 5.0)
        ratio_filter = st.slider("Maximum Student-Faculty Ratio", 6.0, 20.0, 12.0)

    # Apply filters
    filtered_df = df.copy()
    if type_filter != "All":
        filtered_df = filtered_df[filtered_df["Type"] == type_filter]
    filtered_df = filtered_df[filtered_df["Tuition_clean"] <= tuition_max]
    filtered_df = filtered_df[filtered_df["International_clean"] >= intl_filter]
    filtered_df = filtered_df[filtered_df["Ratio_clean"] <= ratio_filter]

    # Show results
    st.markdown("### 📊 Matching Universities")
    st.dataframe(filtered_df.drop(columns=["Tuition_clean", "International_clean", "Ratio_clean"]))

# -----------------------------------------------------------
# 🆚 COMPARE TOP 3 SECTION (coming soon)
# -----------------------------------------------------------

elif mode == "Compare My Top 3 Universities":
    st.markdown("🚧 This feature is coming soon! You’ll be able to choose three universities and compare them side-by-side.")