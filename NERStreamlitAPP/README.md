# Custom NER Streamlit App
This Streamlit app allows users to explore **custom Named Entity Recognition (NER)** using [spaCy](https://spacy.io/). Users are able to enter their unique text, choose one of the sample texts given, and define custom entity labels and patterns using spaCy’s `EntityRuler`, and view color-coded entity highlights.
 
- - - 
## Project Overview
This unique NER app was created as part of a project in my "Elements of Computing II" class, with the purpose of exploring the skills we have learned, using Python, spaCy, and Streamlit

* Named Entity Recognition (NER) is a very important concept in natural language processing, and it involves identifying and classifying key elements like names of people, organizations, countries, and more. This app was built using spaCy’s **EntityRuler**, which lets users define their own rules for entity recognition. It’s a simple and interactive way to learn how spaCy tags text, and how rule-based NER work with Machine Learning models. 

- - - 

## How to Run the App

### Requirements
If you're running the app locally, make sure your `requirements.txt` file includes the following lines:
- streamlit spacy==3.8.4 
- https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.8.0/en_core_web_sm-3.8.0-py3-none-any.whl

### Instructions
1. Open a terminal.
2. Navigate to the project directory where `app.py` is located:
                 cd NERStreamlitApp
3. Run the following command to start the app:
                 streamlit run app.py

The app will automatically open in your default web browser.

### Access the Live App:
[Launch the App](https://scohenma-cohen-python-portfolio-nerstreamlitappapp-yfd209.streamlit.app/)
- - - 
### App Features
* Pick a sample or write your own: Choose from a few current events or paste your own text to explore it. 
* Create and type in your own entity label and pattern. The instruction here is to type in the kind of thing you want to detect (like PERSON or ORG) and the exact word or phrase to match.
* Add your rule to spaCy’s NER system: Your custom rule gets added to the pipeline so it can be recognized in the text, and see how the app matches and higlights your entities in your original text.

### Example Patterns

| Sample Text | Suggested Label | Suggested Pattern |
|-------------|------------------|-------------------|
| Stock Market Volatility | `PERSON` | `Trump` |
| Katy Perry Launch | `PERSON` | `Katy Perry` |
| Notre Dame Ranking | `ORG` | `University of Notre Dame` |

### References
* [The Basics of Spacy](https://spacy.pythonhumanities.com/01_01_install_and_containers.html)
* [spaCy Linguistic Annotations](https://spacy.pythonhumanities.com/01_02_linguistic_annotations.html)

