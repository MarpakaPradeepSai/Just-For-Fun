import streamlit as st
import spacy

# Load the pre-trained model
try:
    nlp = spacy.load("en_core_web_trf")
except OSError:
    st.error("Model 'en_core_web_trf' not found. Ensure it is installed via requirements.txt.")
    st.stop()

st.title("NER with en_core_web_trf")
text = st.text_area("Enter text to analyze:")

if text:
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    st.write("### Detected Entities:")
    st.table(entities)
