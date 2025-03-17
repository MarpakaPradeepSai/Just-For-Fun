import streamlit as st
import spacy

# Function to load the spacy model (ensure it's downloaded)
@st.cache_resource  # Use st.cache_resource for efficient model loading
def load_model():
    try:
        nlp = spacy.load("en_core_web_trf")
        return nlp
    except OSError:
        st.error("It seems like 'en_core_web_trf' is not downloaded. Please run: `python -m spacy download en_core_web_trf` in your terminal and restart the app.")
        return None

# Load the spaCy model
nlp = load_model()

st.title("spaCy en_core_web_trf in Streamlit")

user_input = st.text_area("Enter text here:", "This is an example sentence to analyze.")

if nlp is not None and user_input:
    doc = nlp(user_input)

    st.header("Named Entities:")
    if doc.ents:
        for ent in doc.ents:
            st.write(f"- **{ent.text}**:  *{ent.label_}*")
    else:
        st.write("No named entities found in the text.")

    st.header("Sentence Analysis (Example - just sentences):")
    for sent in doc.sents:
        st.write(sent.text)
