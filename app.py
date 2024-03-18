import streamlit as st
from shared_func.pdfplumber_func import *
from shared_func.text_func import *
from shared_func.plot_func import *
from shared_func.pickle_func import *


def main():
    st.title("PDF Text Extractor")

    # File uploader for uploading PDF files
    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

    if uploaded_file is not None:
        # Display the uploaded PDF file
        st.write("Uploaded PDF file:", uploaded_file.name)
        text = extract_text_from_pdf(uploaded_file)

        lst_wrd = clean_text(text, language="english")
        # Display the plots using Streamlit
        st.write("# Most Frequent Words")
        freq_wrd = top_20_words(lst_wrd)
        most_freq_fig = plot_most_freq_wrds(data=freq_wrd)
        st.plotly_chart(most_freq_fig)

        st.write("# Biagram")
        freq_wrd = biagram(lst_wrd)
        biagram_fig = plot_most_freq_wrds(data=freq_wrd)
        st.plotly_chart(biagram_fig)

        st.write("# Word Cloud")
        word_cloud_fig = plot_wrd_cloud(lst_wrd)
        st.pyplot(word_cloud_fig)

if __name__ == "__main__":
    main()
