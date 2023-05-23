import pyperclip
import tempfile
import os
from extract_text import extract_text_from_pdf
from call2llm import get_response, get_continued_response  # Import specific functions instead of importing everything from call2llm
import streamlit as st

def main():
    st.title("AskPDF")

    # Sidebar to display uploaded PDFs
    if st.sidebar.button("Reset Thread"):
        if os.path.exists("config.json"):
            os.remove(os.path.join(".", "config.json"))

    uploaded_files = st.sidebar.file_uploader("Upload PDF files", accept_multiple_files=True, type=["pdf"])
    pdf_files = []

    # Process uploaded PDFs
    for uploaded_file in uploaded_files:
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(uploaded_file.read())
            temp_file_path = temp_file.name

        pdf_files.append((uploaded_file.name, temp_file_path))
    
    # Two-column layout for start and end pages
    col1, col2 = st.columns(2)

    # Convert PDFs to text
    converted_texts = []
    for i, (file_name, file_path) in enumerate(pdf_files):
        # Input fields for start and end pages
        with col1:
            start_page = st.number_input(f"Start Page ({file_name})", min_value=1, value=1, key=f"start_page_{i}")
        with col2:
            end_page = st.number_input(f"End Page ({file_name})", min_value=start_page, value=start_page, key=f"end_page_{i}")

        # Convert PDF to text
        text = extract_text_from_pdf(file_path, start_page, end_page)
        converted_texts.append(text)
    
    # Copy all converted texts to clipboard
    if st.button("Copy text from PDF"):
        combined_text = "\n".join(converted_texts)
        pyperclip.copy(combined_text)
        st.success("All texts copied to clipboard!")

    query = st.text_input("Enter your question")

    if st.button("Ask PDF"):
        response_placeholder = st.empty()
        print("calling llm")
        combined_text = "\n".join(converted_texts)
        response = ""

        if not os.path.exists("config.json"):
            response = get_response(combined_text + query, response_placeholder)
        else:
            response = get_continued_response(query, response_placeholder)
            print(response)

        pyperclip.copy(response)
        
    if st.button("Copy Prompt"):
        combined_text = "\n".join(converted_texts)
        pyperclip.copy(combined_text + query)

    # Delete temporary files
    for _, file_path in pdf_files:
        os.remove(file_path)

if __name__ == "__main__":
    main()
