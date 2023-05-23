# AskPDF (No OpenAI API Key Required)


AskPDF is a Streamlit app that allows you to extract text from uploaded PDF files, ask questions related to the extracted text, and get AI-generated responses. The app uses the OpenAI Language Model to provide answers based on the given text and query.

## Instructions to Run

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/naveenbalachandran/AskPDF.git
   ```

2. Navigate to the project directory:

   ```bash
   cd askpdf
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Run the app:

   ```bash
   streamlit run app.py
   ```

6. The app will open in your default web browser. You can now use it to upload PDF files, extract text, ask questions, and get AI-generated responses.

## Usage

1. Upload PDF files:
   - Click on the "Upload PDF files" button in the sidebar.
   - Select one or more PDF files from your local machine.

2. Convert PDFs to text:
   - For each uploaded PDF file, specify the start and end pages for text extraction.
   - The extracted text will be displayed on the screen.

3. Copy text to clipboard:
   - Click on the "Copy text" button to copy all the extracted text to your clipboard.

4. Ask questions and get responses:
   - Enter your question in the text input field.
   - Click on the "Ask PDF" button to get an AI-generated response based on the extracted text and your question.
   - The response will be displayed on the screen and copied to your clipboard.

5. Copy prompt to clipboard:
   - Click on the "Copy Prompt" button to copy the combined text of all extracted PDFs and your question to your clipboard.

6. Reset the thread:
   - Click on the "Reset Thread" button in the sidebar to reset the conversation thread and start over.

7. Clean up:
   - Once you are done using the app, you can delete the temporary files generated during the process.

## Privacy and Usage Warning

**Important:** In order to make the app work without using an OpenAI API key, the app currently utilizes a GPT-3.5 endpoint exposed by the website https://chat.theb.ai/. Please note that I have no affiliation with this website and cannot vouch for their privacy policies or data security measures. 

When using this app, be cautious about the content you upload and the information you provide. Avoid uploading any sensitive or personal documents as they may be processed by the external endpoint.

If you prefer to use your own OpenAI API key for privacy and security reasons, you can update the `call2llm.py` file in the project. Replace the existing endpoint and implementation with your own API key integration. Please refer to the OpenAI documentation for more information on how to use the OpenAI API.

By using this app, you acknowledge and accept the potential risks associated with using the external GPT-3.5 endpoint and agree to take full responsibility for any data privacy concerns that may arise.

It is strongly recommended to review the privacy policies and terms of service of the external website (https://chat.theb.ai/) before using the app.

Please use the app responsibly and ensure that you comply with any applicable laws and regulations regarding data privacy and security.

## License

This project is licensed under the [MIT License](LICENSE).
