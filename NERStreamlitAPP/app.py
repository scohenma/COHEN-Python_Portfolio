#Installation
!pip install spacy
!python -m spacy download en_core_web_sm


import streamlit as st
import spacy
from spacy.pipeline import EntityRuler
from spacy import displacy
#Load spaCy
nlp = spacy.load('en_core_web_sm')