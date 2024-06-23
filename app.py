
import streamlit as st
from transformers import T5ForConditionalGeneration, T5Tokenizer
from datasets import load_dataset
import re

# Load dataset and preprocess
@st.cache_data
def load_and_preprocess_data():
    data = load_dataset("ccdv/pubmed-summarization")
    return data.map(lambda x: {"article": preprocess(x["article"]), "abstract": preprocess(x["abstract"])})

def preprocess(text):
    text = re.sub(r'\s+', ' ', text)  # Remove multiple spaces
    text = re.sub(r'\[[^]]*\]', '', text)  # Remove references
    text = re.sub(r'\([^)]*\)', '', text)  # Remove parentheses
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    text = text.lower()
    return text

# Initialize T5 model and tokenizer
model_name = "t5-small"
model = T5ForConditionalGeneration.from_pretrained(model_name)
tokenizer = T5Tokenizer.from_pretrained(model_name)

# Function to summarize an article
def summarize_article(article):
    # Preprocess the article if necessary
    article = preprocess(article)

    # Prepare input for the model
    inputs = tokenizer.encode("summarize: " + article, return_tensors="pt", max_length=512, truncation=True)

    # Generate summary
    summary_ids = model.generate(inputs, max_length=150, min_length=30, length_penalty=2.0, num_beams=4, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    return summary

# Streamlit app
def main():
    st.title("PubMed Article Summarizer")

    # Option to upload a file
    uploaded_file = st.file_uploader("Upload an article file (txt)", type="txt")
    
    article = ""
    
    if uploaded_file is not None:
        # Read the uploaded file
        article = uploaded_file.read().decode("utf-8")
        st.text_area("Uploaded Article:", value=article, height=200, disabled=True)
    else:
        # Input box for user to enter article
        article = st.text_area("Or enter the article to summarize:")

    # Button to trigger summarization
    if st.button("Summarize"):
        if article.strip() == "":
            st.error("Please enter a valid article.")
        else:
            # Perform summarization
            summary = summarize_article(article)

            # Display results
            st.subheader("Original Article:")
            st.write(article)
            st.subheader("Summary:")
            st.write(summary)

if __name__ == "__main__":
    main()
