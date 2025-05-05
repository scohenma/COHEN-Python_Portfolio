import streamlit as st

# Title and description
st.title("College Compass")
st.write("An interactive tool to help students compare and choose universities based on their personal priorities.")

# Add a placeholder for future interactivity
st.subheader("Coming soon...")
st.info("This app will help you compare universities by academics, cost, location, rankings, and more!")

# Section: User Preferences
st.header("🔍 Tell us what matters to you")

# Sliders for importance
cost_weight = st.slider("Importance of Cost", 0, 10, 5)
academics_weight = st.slider("Importance of Academics", 0, 10, 5)
location_weight = st.slider("Importance of Location", 0, 10, 5)
rank_weight = st.slider("Importance of Reputation/Ranking", 0, 10, 5)

# Region preference
region = st.selectbox("Preferred Region", ["Any", "Northeast", "Midwest", "South", "West"])

# Major selection
majors = st.multiselect(
    "What majors are you most interested in?",
    ["Computer Science", "Business", "Engineering", "Psychology", "Political Science", "Biology", "Undecided"]
)

# Optional email input (for future contact feature)
email = st.text_input("Enter your email (optional)")

st.success("Thanks! Based on your preferences, we'll recommend universities.")

st.header("Step 1: What matters most to you? 🎓")

# Location preference
location = st.selectbox(
    "Preferred location",
    ["No preference", "Northeast", "South", "Midwest", "West"]
)

# Cost sensitivity
cost_priority = st.slider("How important is tuition cost to you?", 0, 10, 5)

# Academic focus
academic_strength = st.selectbox(
    "Which academic area is most important?",
    ["No preference", "STEM", "Business", "Humanities", "Arts", "Social Sciences"]
)

# Extracurriculars
extracurriculars = st.multiselect(
    "Which extracurriculars are must-haves?",
    ["Football", "Greek Life", "Study Abroad", "Research Opportunities", "Service Organizations", "Robotics/Engineering Clubs"]
)

# Class size
class_size = st.radio(
    "Preferred class size",
    ["No preference", "Small (<5,000)", "Medium (5,000–15,000)", "Large (15,000+)"]
)

# Public vs Private
school_type = st.radio(
    "Do you prefer public or private schools?",
    ["No preference", "Public", "Private"]
)

