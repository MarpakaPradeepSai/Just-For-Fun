import streamlit as st
import spacy

# Load the en_core_web_trf model
@st.cache_resource
def load_model():
    nlp = spacy.load("en_core_web_trf")
    return nlp

# Initialize the model
nlp = load_model()

# Streamlit app
st.title("NLP with en_core_web_trf Model")
st.write("Enter text to analyze using spaCy's en_core_web_trf model.")

# Text input
user_input = st.text_area("Input Text")

# Process the text when the button is clicked
if st.button("Analyze"):
    if user_input:
        # Process the input text with the model
        doc = nlp(user_input)
        
        # Display results
        st.subheader("Named Entities")
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        if entities:
            for entity, label in entities:
                st.write(f"Entity: {entity}, Label: {label}")
        else:
            st.write("No entities found.")
    else:
        st.warning("Please enter some text to analyze.")
