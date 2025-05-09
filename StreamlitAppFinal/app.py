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

As a Notre Dame student, I’ve often heard people say, "There’s just something about this place." That something — a unique mix of values, community, purpose, and spirit — is what inspired me to build this tool.

Through my research, I found 10 universities that share many of those same qualities. While this app offers just a snapshot of what each school has to offer, I truly believe they’re exceptional options worth exploring. Consider this your sign to learn more about them — and maybe even add a few to your application list!

This app is designed to help students discover universities where excellence meets mission — places that don’t just educate, but inspire.

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

import streamlit as st
import matplotlib.pyplot as plt

st.markdown("#### 🔍 What would you like to do?")
mode = st.radio(
    "Choose one:",
    ["Help Me Decide Where to Apply", "Learn More About Each One"]
)

if mode == "Help Me Decide Where to Apply":
    st.markdown("#### 🎯 Let’s Find Your Fit")
    st.write("Use the filters below to narrow down the schools that match your goals:")

    col1, col2 = st.columns(2)

    with col1:
        type_filter = st.selectbox(
            "Select University Type", 
            ["All", "Public", "Private"],
            help="Choose whether you want to view public, private, or all universities."
        )

        tuition_max = st.slider(
            "Max Tuition ($)",
            min_value=40000,
            max_value=70000,
            value=65000,
            help="Set the highest tuition you're willing to consider."
        )

    with col2:
        intl_filter = st.slider(
            "Minimum % of International Students",
            min_value=0.0,
            max_value=20.0,
            value=5.0,
            help="Only show schools with at least this percent of international students."
        )

        ratio_filter = st.slider(
            "Maximum Student-Faculty Ratio",
            min_value=6.0,
            max_value=20.0,
            value=12.0,
            help="Lower ratios typically mean smaller class sizes and more faculty access."
        )

    st.markdown("#### 📌 Summary of Current Filters")
    st.info(
        f"You’re viewing universities with the following filters:\n\n"
        f"🎓 Type: **{type_filter}**  \n"
        f"💸 Max Tuition: **${tuition_max:,}**  \n"
        f"🌍 Min % Intl Students: **{intl_filter}%**  \n"
        f"👩‍🏫 Max Student-Faculty Ratio: **{ratio_filter}**"
    )

    # Apply filters
    filtered_df = df.copy()
    if type_filter != "All":
        filtered_df = filtered_df[filtered_df["Type"] == type_filter]
    filtered_df = filtered_df[filtered_df["Tuition_clean"] <= tuition_max]
    filtered_df = filtered_df[filtered_df["International_clean"] >= intl_filter]
    filtered_df = filtered_df[filtered_df["Ratio_clean"] <= ratio_filter]


    # Show results
    st.markdown("#### 📊 Matching Universities")
    st.dataframe(filtered_df.drop(columns=["Tuition_clean", "International_clean", "Ratio_clean", "Mission", "Athletics"]))

    # Visualizations in Tabs
    st.markdown("#### 📊 Explore Key Insights from Your Matches")

    if not filtered_df.empty:
        tab1, tab2, tab3 = st.tabs(["💸 Tuition Distribution", "🏛️ Public vs Private", "🌍 International Students"])

        with tab1:
            fig1, ax1 = plt.subplots()
            ax1.hist(filtered_df["Tuition_clean"], bins=8, color="lightblue")
            ax1.set_title("Tuition Distribution Among Matching Schools")
            ax1.set_xlabel("Tuition ($)")
            ax1.set_ylabel("Number of Universities")
            st.pyplot(fig1)

        with tab2:
            type_counts = filtered_df["Type"].value_counts()
            fig2, ax2 = plt.subplots()
            ax2.pie(type_counts, labels=type_counts.index, autopct="%1.1f%%", startangle=90, colors=["skyblue", "lightgreen"])
            ax2.axis("equal")
            st.pyplot(fig2)

        with tab3:
            intl_sorted = filtered_df.sort_values(by="International_clean", ascending=False)
            fig3, ax3 = plt.subplots()
            ax3.bar(intl_sorted["University"], intl_sorted["International_clean"], color="lightblue")
            ax3.set_xticklabels(intl_sorted["University"], rotation=45, ha="right")
            ax3.set_ylabel("% of International Students")
            ax3.set_title("Global Diversity Across Matching Universities")
            st.pyplot(fig3)
    else:
        st.info("No results to visualize — adjust your filters above.")

elif mode == "Learn More About Each One":
    st.markdown("## 🏛️ Discover Each University")

    selected_uni = st.selectbox("Choose a university to learn more about:", df["University"].unique())
    uni_data = df[df["University"] == selected_uni].iloc[0]

    st.markdown("#### 🧭 Basic Information")
    st.write(uni_data["Mission"])

    st.image(campus_images[selected_uni], caption="📍 Campus View", use_column_width=True)

    st.markdown(f"#### 🎓 {uni_data['University']}")

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

    if selected_uni == "University of Notre Dame":
        st.markdown("#### 💬 Personal Note from the Creator")
        st.success(
            "I am a current junior here, and would not imagine being anywhere else. "
            "This app is just a preview of the basic information — there is so much more to this place. "
            "There’s truly no place like it.\n\n"
            "**If you have any questions about the application process, please feel free to reach out.**\n\n"
            "**GO IRISH! ☘️**"
        )