# Bayyenah
Bayyenah is a web platform for newcomers to review job contracts before signing. Users upload PDFs or images; OCR extracts the text. AI analysis (powered by ChatGPT) checks each clause against labor laws, classifying them by color: green for fair, Yellow for ambiguous, and Red for unfair. Clear explanations ensure transparency and protect rights.

## Features
- Upload contracts in PDF or image format
- OCR extracts text for analysis
- AI-powered clause classification and explanations
- Color-coded risk indicators: Green (fair), Yellow (ambiguous), Red (unfair)

## Requirements
- Python 3.8+
- Flask
- Pillow
- pytesseract
- pdf2image
- playwright
- Tesseract OCR (must be installed separately)
- Node.js (for playwright)

## Install dependencies:
pip install -r requirements.txt

## Run the app:
1. Open the Command Prompt (cmd) and run this command, replacing the path if your Chrome is installed elsewhere:
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\chrome-dev-session"
2. In the opened Chrome window, log in to your ChatGPT account and send any message in the chat to activate the session.
3. Then, in a separate terminal (I use Python terminal), run the backend server with:
python backend.py
4. After the server starts, you will see a local website link. Open it in your browser to start uploading and analyzing your contracts!


## License
This project is licensed under the MIT License.

