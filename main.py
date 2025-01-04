import streamlit as st
from PyPDF2 import PdfReader #for reading the pdf
from chains import Chain #custom module for interacting with llm
from utils import clean_text 

def extract_text_from_pdf(pdf_file):
    reader = PdfReader(pdf_file) #opens the pdf dor reading
    text = "" 
    for page in reader.pages: # retrieves pages in pdf
        text += page.extract_text() #extracts the text from each page
    return text

#PDF Questioning Frontend
def create_pdf_qa_app(llm, clean_text):
    st.title("📄 PDF Question Answering")
    
    # Upload PDF
    uploaded_file = st.file_uploader("Upload a PDF file:", type="pdf")
    if uploaded_file:
        # Extract text
        raw_text = extract_text_from_pdf(uploaded_file)
        cleaned_text = clean_text(raw_text)
        st.success("PDF content loaded successfully!")
        
        # Ask questions
        question = st.text_input("Ask a question about the document:")
        if st.button("Submit"):
            try:
                answer = llm.answer_question(cleaned_text, question)
                st.write("### Answer:")
                st.write(answer)
            except Exception as e:
                st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    chain = Chain()
    st.set_page_config(layout="wide", page_title="PDF QA", page_icon="📄")
    create_pdf_qa_app(chain, clean_text)
