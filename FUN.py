import spacy
import streamlit as st

# Load the transformer model
try:
    nlp = spacy.load("en_core_web_trf")
except OSError:
    st.error("Model not found. Please run: python -m spacy download en_core_web_trf")
    st.stop()

st.title("Transformer NER with spaCy")
st.write("Enter text to extract named entities using the en_core_web_trf model")

text = st.text_area("Input Text", height=200)
if st.button("Process"):
    if text.strip():
        doc = nlp(text)
        st.subheader("Named Entities")
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        if entities:
            st.table(entities)
        else:
            st.write("No entities found")
    else:
        st.warning("Please enter some text")
