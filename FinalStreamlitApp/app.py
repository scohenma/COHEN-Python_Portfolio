import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# Loading data
df = pd.read_csv("FinalStreamlitApp/universities_final_cleaned.csv")


# Attaching Campus photos
campus_images = {
   "University of Notre Dame": "FinalStreamlitApp/nd.jpg",
   "Georgetown University": "FinalStreamlitApp/georgetown.jpg",
   "Boston College": "FinalStreamlitApp/bostoncollege.jpg",
   "Villanova University": "FinalStreamlitApp/villanova.jpg",
   "University of Texas at Austin": "FinalStreamlitApp/utaustin.jpg",
   "Duke University": "FinalStreamlitApp/duke.jpg",
   "Santa Clara University": "FinalStreamlitApp/santaclara.jpg",
   "Saint Louis University": "FinalStreamlitApp/stlouis.jpg",
   "University of Virginia": "FinalStreamlitApp/uvirginia.jpg",
   "Syracuse University": "FinalStreamlitApp/syracuse.jpg"
   }


# Cleaning column names
df.columns = df.columns.str.strip()


# Ensuring columns are correct
df.columns = [
   "University", "Rank", "Location", "Undergrad Enrollment", "Tuition",
   "International Students (%)", "Student-Faculty Ratio", "Athletics", "Mission", "Type"
]


# Converting numerical fields
df["International_clean"] = df["International Students (%)"].astype(float)
df["Ratio_clean"] = df["Student-Faculty Ratio"].astype(float)
df["Tuition_clean"] = df["Tuition"].astype(float)


# Introduction


st.title("University Comparison Tool")


st.markdown("""
### 🎓 Welcome to the University Explorer App
          
As a Notre Dame student, I’ve often heard people say, "There’s just something about this place." That something — a unique mix of values, community, purpose, and spirit — is what inspired me to build this tool.


Through my research, I found 10 universities that share many of those same qualities. While this app offers just a snapshot of what each school has to offer, I truly believe they’re exceptional options worth exploring. Consider this your sign to learn more about them — and maybe even add a few to your application list!


This app is designed to help students discover universities where excellence meets mission — places that don’t just educate, but inspire.


---


### 🌟 Featured Universities
""")


# Listing universities
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




#User Option: Decide or Learn More


#import
import streamlit as st
import matplotlib.pyplot as plt


st.markdown("#### 🔍 What would you like to do?")
mode = st.radio(
   "Choose one:",
   ["Help Me Decide Where to Apply", "Learn More About Each One"]
)


if mode == "Help Me Decide Where to Apply":
   st.markdown("#### 🎯 Let’s Find Your Fit")
   st.write("Answer a few questions below to personalize your university matches:")


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


   # Personalized filter questions
   st.markdown("#### 🧠 Personalize Your Priorities")


   care_about_diversity = st.radio(
       "Do you care about international diversity on campus?",
       ["Yes", "No"],
       help="We'll only filter for % of international students if this matters to you."
   )


   if care_about_diversity == "Yes":
       intl_filter = st.slider(
           "Minimum % of International Students",
           0.0, 20.0, 5.0,
           help="Only show schools with at least this percent of international students."
       )
   else:
       intl_filter = 0.0


   care_about_ratio = st.radio(
       "Do you care about small class sizes and more faculty interaction?",
       ["Yes", "No"],
       help="This controls the student-faculty ratio filter."
   )


   if care_about_ratio == "Yes":
       ratio_filter = st.slider(
           "Maximum Student-Faculty Ratio",
           6.0, 20.0, 12.0,
           help="Lower ratio means smaller classes and more personalized attention."
       )
   else:
       ratio_filter = 100.0


   st.markdown("#### Summary of Current Filters")
   st.info(
       f"You’re viewing universities with the following filters:\n\n"
       f"Type: **{type_filter}**  \n"
       f"Max Tuition: **${tuition_max:,}**  \n"
       f"Min % Intl Students: **{intl_filter}%**  \n"
       f"Max Student-Faculty Ratio: **{ratio_filter}**"
   )


   # Applying filters
   filtered_df = df.copy()
   if type_filter != "All":
       filtered_df = filtered_df[filtered_df["Type"] == type_filter]
   filtered_df = filtered_df[filtered_df["Tuition_clean"] <= tuition_max]
   filtered_df = filtered_df[filtered_df["International_clean"] >= intl_filter]
   filtered_df = filtered_df[filtered_df["Ratio_clean"] <= ratio_filter]


   # Showing results
   st.markdown("#### 📊 Matching Universities")
   st.dataframe(filtered_df.drop(columns=["Tuition_clean", "International_clean", "Ratio_clean", "Mission", "Athletics"]))


   # Visualizations in Tabs
   st.markdown("#### Explore Key Insights from Your Matches")


   if not filtered_df.empty:
       tab1, tab2, tab3 = st.tabs(["Tuition Distribution", "Public vs Private", "International Students"])


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
           ax2.pie(type_counts, labels=type_counts.index, autopct="%1.1f%%", startangle=90, colors=["lightblue", "lightgreen"])
           ax2.set_title("Private Vs Public Schools")
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
   st.markdown("#### 🏛️ Discover Each University")


   selected_uni = st.selectbox("Choose a university to learn more about:", df["University"].unique())
   uni_data = df[df["University"] == selected_uni].iloc[0]


   mission_= {
       "University of Notre Dame": "A private Catholic university in Indiana, famous for its Golden Dome, rich traditions, and strong football culture. Known for academic excellence and a deep sense of community.",
       "Georgetown University": "Located in Washington, D.C., it’s the oldest Jesuit university in the U.S. Known for international relations, law, and politics, with alumni that include U.S. presidents and global leaders.'",
       "Boston College": "A Jesuit university in Massachusetts with a strong liberal arts tradition. Offers a beautiful campus and a tight-knit community. Known for business, education, and Division I athletics.",
       "Villanova University": "Founded by the Augustinian order in Pennsylvania, Villanova blends rigorous academics with strong values",
       "University of Texas at Austin": "An iconic public university in Texas, UT Austin is a powerhouse in research, innovation, and sports. Home of the Longhorns and the famous tower overlooking the city skyline.",
       "Duke University": "A prestigious private university in North Carolina, Duke excels in academics and athletics. Famous for its Gothic architecture, medical center, and basketball legacy.",
       "Santa Clara University": "A Jesuit university in the heart of Santa Clara. Combines liberal arts and tech-oriented education with a mission rooted in social justice and innovation.",
       "Saint Louis University": "A Catholic, Jesuit university located in Missouri. Known for its strong programs in health sciences, law, service learning, and research.",
       "University of Virginia": "Founded by Thomas Jefferson in Charlottesville, UVA is steeped in history. Academically elite, with a strong community.",
       "Syracuse University": "A private research university in New York with a vibrant student life and strong academic programs."
   }

   st.markdown("#### About")
   st.markdown(mission_[selected_uni].replace("\n", "\n\n"))

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
  
   fun_facts = {
       "University of Notre Dame": "- The Golden Dome is covered in real gold leaf.\n- Students avoid walking up the Main Building steps until graduation.\n- Helmets worn by the football team are painted with real gold dust.",
       "Georgetown University": "- Students do the 'Healy Howl' after a Halloween Exorcist screening.\n- Jack the Bulldog mascot rides a golf cart around campus.\n- 'Hoya Saxa' is a cheer combining Greek and Latin meaning 'What Rocks!'",
       "Boston College": "- Students line the Boston Marathon route every April.\n- The Red Bandanna Game honors 9/11 hero Welles Crowther.\n- Their mascot is Baldwin the Eagle.",
       "Villanova University": "- The giant Oreo sculpture is a campus landmark.\n- Hosts the largest student-run Special Olympics in the world.\n- Holds an annual Day of Service that cancels all classes.",
       "University of Texas at Austin": "- Seeing an albino squirrel before exams brings good luck.\n- Bevo the mascot got his name from a branding prank.\n- Big Bertha is UT’s massive 8-foot bass drum.",
       "Duke University": "- Students camp for weeks in Krzyzewskiville to get basketball tickets.\n- Home to the world’s largest lemur research center.\n- Blue Devils are named after WWI French soldiers.",
       "Santa Clara University": "- Built around a Spanish mission church from 1777.\n- First Catholic university in California to admit women.\n- During finals, students yell 'Wake up, Swig!' outside dorms.",
       "Saint Louis University": "- First university west of the Mississippi River.\n- The Billiken mascot is based on a 1908 good-luck doll.\n- Completed the first legal forward pass in football history.",
       "University of Virginia": "- Rotunda and Lawn are a UNESCO World Heritage Site.\n- Secret societies like the Seven Society leave cryptic symbols.\n- Streaking the Lawn is a student tradition before graduation.",
       "Syracuse University": "- Only school with orange as its sole official color.\n- Otto the Orange is a smiling fruit mascot.\n- Number 44 is legendary in SU football and ZIP code."
   }


   st.markdown("#### Fun Facts")
   st.markdown(fun_facts[selected_uni].replace("\n", "\n\n"))


   st.markdown("#### Additional Information and Final Advice")
   with st.expander("📚 Want to know more about academics?"):
       st.markdown("Here are the most popular majors offered at this university:")


       majors_by_university = {
           "University of Notre Dame": ["Political Science", "Psychology", "English", "Finance", "Science/Pre-professional"],
           "Boston College": ["Finance", "Economics", "Neuroscience", "Psychology", "Communication"],
           "Georgetown University": ["Political Science and Government", "International Relations", "Finance", "Economics", "Psychology"],
           "University of Virginia": ["Liberal Arts and Sciences", "Social Sciences", "Engineering", "Business/Commerce", "Computer and Info Systems"],
           "Villanova University": ["Finance", "General Studies", "Registered Nursing", "Speech Communication and Rhetoric"],
           "University of Texas at Austin": ["Engineering", "Business", "Biological and Biomedical Sciences", "Communication & Journalism", "Social Sciences"],
           "Duke University": ["Computer and Information Science", "Social Sciences", "Engineering", "Biological Sciences", "Mathematics and Statistics"],
           "Santa Clara University": ["Finance", "Speech Communication", "Psychology", "Math & Computer Science", "Marketing"],
           "Saint Louis University": ["Nursing", "Lab Technician", "Kinesiology", "Biology", "Finance"],
           "Syracuse University": ["Information Science", "Psychology", "Finance", "Economics", "Political Science"]
       }


       if selected_uni in majors_by_university:
           for major in majors_by_university[selected_uni]:
               st.markdown(f"- {major}")
       else:
           st.write("No data available for this university.")
   with st.expander("📘 Application Tips & Tricks"):
       st.markdown("Get tailored advice based on where you are in your high school journey:")


       grade_level = st.selectbox(
           "What grade are you in?",
           ["Freshman or Sophomore", "Junior", "Senior"]
       )


       if grade_level == "Freshman or Sophomore":
           st.markdown("""
           - Focus on building a strong academic foundation — your GPA **starts now**.\n
           - Get involved in a few extracurriculars you care about. Depth > quantity!\n
           - Start exploring what majors or subjects excite you.\n
           - Try to take **challenging courses** if possible — honors, AP, IB, etc.\n
           - Consider starting SAT/ACT prep **early and casually** (apps, practice questions).\n
           - Begin documenting awards, clubs, and activities in a spreadsheet.\n
           - Build good relationships with teachers who may write recommendations later.\n
           """)


       elif grade_level == "Junior":
           st.markdown("""
           - **Start seriously preparing** for the SAT/ACT — use practice exams and review books.\n
           - Research universities that fit your interests, values, and goals.\n
           - Attend college fairs or virtual info sessions.\n
           - Aim to take leadership roles in the activities you care about.\n
           - Continue keeping your grades strong — junior year is often the most reviewed.\n
           - Talk to upperclassmen about their college process and what they’d do differently.\n
           - Visit local campuses or do virtual tours to get a feel for different environments.\n
           """)


       elif grade_level == "Senior":
           st.markdown("""
           - The summer before senior year: build your **college list** and organize deadlines.\n
           - Create a new, professional email just for college apps to stay organized.\n
           - Talk with your school counselor for personalized suggestions and advice.\n
           - Start brainstorming and drafting your **personal statement/essays** early.\n
           - Ask for **recommendation letters** before the school year starts — give your teachers time!\n
           - Schedule any final SAT/ACT test dates as early as possible.\n
           - Don’t be afraid to **email students, alumni, or admissions counselors** — they’re often eager to help!\n
           - Visit campuses if you can — or explore them through online videos or Instagram reels.\n
           - Most importantly: **Be yourself in the application**. You will end up where you need to!.\n
           """)


   if selected_uni == "University of Notre Dame":
       st.markdown("#### 💬 Personal Note from the Creator")
       st.success(
           "I am a current junior here, and would not imagine being anywhere else. "
           "This app is just a preview of the basic information — there is so much more to this place. "
           "There’s truly no place like it. I really encourage you to apply! \n\n"
           "**If you have any questions about the application process, please feel free to reach out.**\n\n"
           "**GO IRISH! ☘️**"
       )

