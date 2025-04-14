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
st.write("This app allows you to explore custom Named Entity Recognition using SpaCy by uploading and exploring your own text!")

#User inputs
st.subheader("Step 1 - Upload your custom text")
text = st.text_area("Paste your text here:")

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