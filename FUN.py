import streamlit as st
import spacy

# Load the en_core_web_trf model
nlp = spacy.load("en_core_web_trf")

# Streamlit app
st.title("NLP with en_core_web_trf")

# Get user input
text = st.text_area("Enter some text:", height=200)

if st.button("Analyze"):
    # Process the text using the en_core_web_trf model
    doc = nlp(text)

    # Display the results
    st.subheader("Named Entities:")
    for ent in doc.ents:
        st.write(f"{ent.text} ({ent.label_})")

    st.subheader("Part-of-Speech Tags:")
    for token in doc:
        st.write(f"{token.text}: {token.pos_}")
