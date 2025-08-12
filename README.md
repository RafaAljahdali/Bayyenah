# Bayyenah
Bayyenah is a web-based platform that enables individuals new to the job market to review and understand their employment contracts before signing. Users can upload contracts in PDF or image format, which are processed using OCR to extract text. An AI-powered legal analysis (powered by ChatGPT) then examines each clause, checks compliance with national labor laws, and classifies them using a color-coded system: Green for fair and clear, Yellow for ambiguous and may require clarification, and Red for potentially unfair. Plain-language explanations are provided for every clause to promote transparency, protect employee rights, and prevent exploitation.

## Features
- Upload contracts in PDF or image format
- OCR extracts text for analysis (English and Arabic)
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

