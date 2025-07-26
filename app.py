# Bayyenah - Legal Contract Analyzer System (Simple and Free Version)
# Tools: Python, Streamlit, Tesseract OCR, HuggingFace Transformers
# Hosting: Google Colab for model + Streamlit Cloud for interface

import streamlit as st
import pytesseract
from PIL import Image
from pdf2image import convert_from_bytes
from transformers import pipeline

# Load AI Model (Zero-shot classifier)
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

# Function to extract text from PDF or image
def extract_text(file):
    if file.type == "application/pdf":
        images = convert_from_bytes(file.read())
        text = "\n".join([pytesseract.image_to_string(img) for img in images])
    else:
        image = Image.open(file)
        text = pytesseract.image_to_string(image)
    return text

# Function to classify clause
def classify_clause(text):
    labels = ["fair", "needs clarification", "exploitative"]
    result = classifier(text, candidate_labels=labels)
    top = result['labels'][0]
    if top == "fair":
        color = "green"
    elif top == "needs clarification":
        color = "orange"
    else:
        color = "red"
    return top, color

# Streamlit UI
st.set_page_config(page_title="Bayyenah - Contract Analyzer", layout="centered")
st.title("📄 Bayyenah - Employment Contract Analyzer")
st.markdown("""
Upload your employment contract (image or PDF) and let our AI help you understand the clauses with color-coded analysis:
- 🟢 Fair Clause  
- 🟠 Needs Clarification  
- 🔴 Potentially Exploitative
""")

uploaded_file = st.file_uploader("Upload Contract (PDF/Image)", type=["pdf", "png", "jpg", "jpeg"])

if uploaded_file:
    with st.spinner("Analyzing contract..."):
        full_text = extract_text(uploaded_file)
        clauses = [c.strip() for c in full_text.split(".\n") if len(c.strip()) > 20]  # simple clause split
        for clause in clauses:
            label, color = classify_clause(clause)
            st.markdown(
                f"<div style='background-color:{color};padding:10px;border-radius:10px;margin:5px 0;'>{clause}<br><b>Classification:</b> {label}</div>",
                unsafe_allow_html=True
            )
