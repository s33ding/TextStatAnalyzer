import streamlit as st
from shared_func.pdfplumber_func import *
from shared_func.text_func import *

def main():
    st.title("PDF Text Extractor")

    # File uploader for uploading PDF files
    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

    if uploaded_file is not None:
        # Display the uploaded PDF file
        st.write("Uploaded PDF file:", uploaded_file.name)

        # Extract text from the uploaded PDF file
        with pdfplumber.open(uploaded_file) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text()

        # Display the extracted text
        st.subheader("Top 20 words:")
        words = top_20_words(text)
        st.write(words)

if __name__ == "__main__":
    main()
