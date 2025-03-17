import streamlit as st
import spacy
from spacy import displacy

@st.cache_resource
def load_model():
    return spacy.load("en_core_web_trf")

nlp = load_model()

st.title("NLP Analysis with en_core_web_trf")
st.write("Enter text below to analyze with spaCy's transformer model")

text = st.text_area("Input Text", height=200)

if st.button("Analyze"):
    if text.strip():
        doc = nlp(text)
        
        # Display entities
        st.header("Named Entities")
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        st.table(entities)
        
        # Display dependency parse visualization
        st.header("Text Analysis")
        html = displacy.render(doc, style="ent")
        st.markdown(html, unsafe_allow_html=True)
    else:
        st.warning("Please enter some text to analyze")
