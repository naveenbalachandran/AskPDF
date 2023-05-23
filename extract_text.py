from PyPDF2 import PdfReader
import re

def extract_text_from_pdf(file_path, start_page, end_page):
    with open(file_path, 'rb') as file:
        pdf_reader = PdfReader(file)
        num_pages = len(pdf_reader.pages)

        # Validate start and end page values
        if start_page < 1 or start_page > num_pages:
            st.error("Invalid start page!")
            return ""
        if end_page < start_page or end_page > num_pages:
            st.error("Invalid end page!")
            return ""

        text = ""
        for page_num in range(start_page - 1, end_page):
            page = pdf_reader.pages[page_num]
            extracted_text = page.extract_text()
            # Remove extra whitespaces and newlines using regular expressions
            cleaned_text = re.sub(r'\s+', ' ', extracted_text)
            text += cleaned_text.strip()

        return text
