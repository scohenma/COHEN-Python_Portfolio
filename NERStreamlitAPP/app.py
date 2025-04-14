# Setup Environment 
import pandas as pd
import streamlit as st
import spacy
from spacy.pipeline import EntityRuler
from spacy import displacy

#Load spaCy model
nlp = spacy.load('en_core_web_sm')

#Set the title
st.title("Custom NER Interactive App")
st.write("This app lets you explore custom Named Entity Recognition (NER) using spaCy. Upload or paste your own text, define your own entity rules, and see how NER highlights the people, places, and things in your writing!")

#User inputs
# Step 1: Upload or paste your text
st.subheader("Step 1: Upload or paste your text")

sample_options = [
    "Write your own",
    "Sample 1: Stock market volatility",
    "Sample 2: Katy Perry's space launch",
    "Sample 3: Notre Dame in Forbes ranking"
]

sample_choice = st.selectbox("Choose a sample or write your own:", sample_options)

if sample_choice == "Sample 1: Stock market volatility":
    st.caption("Try label: PERSON and pattern: Trump")
    text = "It’s been a week of uncertainty and volatility in the stock market as  President Trump introduces new tariff policies impacting global trade."

elif sample_choice == "Sample 2: Katy Perry's space launch":
    st.caption("Try label: PERSON and pattern: Katy Perry")
    text = "Katy Perry joined the all-female crew of Blue Origin's latest space mission, which launched and landed successfully earlier this week."

elif sample_choice == "Sample 3: Notre Dame in Forbes ranking":
    st.caption("Try label: ORG and pattern: University of Notre Dame")
    text = "The University of Notre Dame was recently named America’s best large employer by Forbes, praised for its workplace culture and leadership."

else:
    text = st.text_area("Paste your text below:", height=200)

st.subheader("Step 2 - Defining the custom entity")
label = st.text_input("Entity Label:")
pattern = st.text_input("Entity Pattern:")

# Step 3: Run the NER pipeline when the user clicks the button
if st.button("Run EntityRuler"):
    if text and label and pattern:

        # Load spaCy model
        nlp = spacy.load("en_core_web_sm")

        # Format the pattern
        custom_patterns = [{"label": label.upper(), "pattern": pattern}]

# Check if the "ner" pipe exists. If it does, add the EntityRuler before it.
        if "ner" in nlp.pipe_names:
    # If entity_ruler already exists, simply add patterns to it.
            try:
                ruler = nlp.get_pipe("entity_ruler")
            except Exception:
                ruler = nlp.add_pipe("entity_ruler", before="ner")
            ruler.add_patterns(custom_patterns)
        else:
    # If the NER component does not exist, add both the EntityRuler and the NER component.
            ruler = nlp.add_pipe("entity_ruler")
            ruler.add_patterns(custom_patterns)
            ner = nlp.add_pipe("ner")

        # Apply the NLP pipeline to the user input text
        doc = nlp(text)

        # Display detected entities
        st.subheader("Detected Entities:")
        for ent in doc.ents:
            st.write(f"{ent.text} ({ent.label_})")

        # Highlight entities in the original text
        st.subheader("Entity Highlights:")
        html = displacy.render(doc, style="ent", jupyter=False)
        st.markdown(html, unsafe_allow_html=True)
    else:
        st.warning("Please make sure to fill in all the fields above.")