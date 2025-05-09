import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("universities_final_cleaned.csv")

# Campus photos
campus_images = {
    "University of Notre Dame": "nd.jpg",
    "Georgetown University": "georgetown.jpg",
    "Boston College": "bostoncollege.jpg",
    "Villanova University": "villanova.jpg",
    "University of Texas at Austin": "utaustin.jpg",
    "Duke University": "duke.jpg",
    "Santa Clara University": "santaclara.jpg",
    "Saint Louis University": "stlouis.jpg",
    "University of Virginia": "uvirginia.jpg",
    "Syracuse University": "syracuse.jpg"
    }

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
# 🧭 User Option: Decide or Learn More
# -----------------------------------------------------------

st.markdown("### 🔍 What would you like to do?")
mode = st.radio(
    "Choose one:",
    ["Help Me Decide Where to Apply", "Learn More About Each One"]
)

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
    st.dataframe(filtered_df.drop(columns=["Tuition_clean", "International_clean", "Ratio_clean", "Mission", "Athletics"]))
    
    #Optional Comparison Chart
    show_charts = st.checkbox("📈 Show Comparison Charts")


if show_charts and not filtered_df.empty:
    st.markdown("### Undergrad Enrollment Comparison")
    tuition_chart = filtered_df[["University", "Undergrad Enrollment"]].sort_values(by="Undergrad Enrollment", ascending=False)
    st.bar_chart(tuition_chart.set_index("University"))

    st.markdown("### Student-Faculty Ratio")
    ratio_chart = filtered_df[["University", "Student-Faculty Ratio"]].sort_values(by="Student-Faculty Ratio")
    st.bar_chart(ratio_chart.set_index("University"))


elif mode == "Learn More About Each One":
    st.markdown("## 🏛️ Discover Each University")

    selected_uni = st.selectbox("Choose a university to learn more about:", df["University"].unique())
    uni_data = df[df["University"] == selected_uni].iloc[0]

    st.image(campus_images[selected_uni], caption="📍 Campus View", use_column_width=True)

    st.markdown(f"### 🎓 {uni_data['University']}")
  
    # Website links dictionary
    university_links = {
        "University of Notre Dame": "https://www.nd.edu",
        "Georgetown University": "https://www.georgetown.edu",
        "Boston College": "https://www.bc.edu",
        "Villanova University": "https://www1.villanova.edu",
        "University of Texas at Austin": "https://www.utexas.edu",
        "Duke University": "https://www.duke.edu",
        "Santa Clara University": "https://www.scu.edu",
        "Saint Louis University": "https://www.slu.edu",
        "University of Virginia": "https://www.virginia.edu",
        "Syracuse University": "https://www.syracuse.edu"
    }
    st.markdown(f"🔗 [Visit Official Website]({university_links[selected_uni]})")

    # Fun facts dictionary
    fun_facts = {
        "University of Notre Dame": "The Golden Dome is covered in real gold leaf!",
        "Georgetown University": "It’s the oldest Catholic and Jesuit institution in the U.S.",
        "Boston College": "Their mascot is Baldwin the Eagle.",
        "Villanova University": "It was founded in 1842 by the Order of Saint Augustine.",
        "University of Texas at Austin": "Bevo, the longhorn steer, is their beloved mascot.",
        "Duke University": "Students camp out for weeks to get basketball tickets (Krzyzewskiville).",
        "Santa Clara University": "It has a working mission church on campus!",
        "Saint Louis University": "Its mascot is a mysterious blue creature called the Billiken.",
        "University of Virginia": "Founded by Thomas Jefferson himself.",
        "Syracuse University": "Otto the Orange is one of the most unique mascots in college sports."
    }
    st.markdown("#### 🤩 Fun Fact")
    st.info(fun_facts[selected_uni])