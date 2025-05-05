import streamlit as st
import pandas as pd

# Set page title and intro text
st.set_page_config(page_title="College Compass", layout="wide")
st.title("🎓 College Compass")
st.markdown("Welcome! Are you deciding where to go to college? This tool helps you explore and compare top universities based on your goals.")

# Step 1: User selects their goal
st.subheader("What stage are you at?")
user_path = st.radio(
    "Choose one of the following options:",
    ("I already know my options — help me compare them", 
     "I haven’t applied yet — help me build my college list")
)
# Store path selection in session state for routing
st.session_state.user_path = user_path

# Load the dataset
df = pd.read_csv("World University Rankings 2023.csv")

# App title and description
st.title("🏫 College Decision Companion")
st.write("Welcome! Whether you're building your college list or narrowing down where to attend, this app can help you explore, compare, and evaluate universities based on global rankings and key metrics.")

# Option selector
st.subheader("What would you like to do?")
option = st.radio(
    "Choose one:",
    ("🎯 I already know my college options (Compare them)", "📋 I haven’t applied yet (Help me build a list)")
)
if option == "🎯 I already know my college options (Compare them)":
    st.subheader("🔍 Compare Your Top College Choices")

    # Get list of universities from the dataset
    university_list = sorted(df["university_name"].unique())

    # Let user pick 2–3 universities
    selected_universities = st.multiselect(
        "Select universities to compare:",
        options=university_list,
        default=["University of Notre Dame"],  # You can change this default
        help="Choose 2 or 3 schools you’re deciding between"
    )

    # Filter and display results
    if len(selected_universities) >= 2:
        comparison_df = df[df["university_name"].isin(selected_universities)].copy()

        # Clean up columns for display
        comparison_df = comparison_df[["rank", "university_name", "location", "score", "international_students"]]
        comparison_df = comparison_df.sort_values("rank")

        st.write("### 📊 Side-by-Side Comparison")
        st.dataframe(comparison_df.set_index("university_name"))
    
    elif len(selected_universities) == 1:
        st.info("Please select at least 2 universities to compare.")