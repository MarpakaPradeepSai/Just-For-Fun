import streamlit as st
import spacy
import subprocess

# Function to download the model if it's not already downloaded
def download_model(model_name):
    try:
        spacy.load(model_name)
    except OSError:
        subprocess.run(["python", "-m", "spacy", "download", model_name])

# Download the model
download_model("en_core_web_trf")

# Load the model
nlp = spacy.load("en_core_web_trf")

# Streamlit app
st.title("Named Entity Recognition with en_core_web_trf")

text = st.text_area("Enter your text here", "Enter text here")

if text != "Enter text here":
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    st.write(entities)
