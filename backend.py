from flask import Flask, request, jsonify, render_template
import os
from PIL import Image
import pytesseract
from pdf2image import convert_from_path
from playwright_script import classify

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files['contract']
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    extracted_text = ""

    if file.filename.lower().endswith('.pdf'):
        images = convert_from_path(filepath)
        for image in images:
            text = pytesseract.image_to_string(image, lang='eng+ara', config="--psm 6")
            extracted_text += text + "\n\n"

    else:
        image = Image.open(filepath)
        extracted_text = pytesseract.image_to_string(image, lang='eng+ara', config="--psm 6")

    prompt = f"""
    أنت محقق قانوني وخبير في عقود العمل. مهمتك تحليل بنود عقد الموظف بدقة وتصنيف كل بند إلى إحدى الفئات الثلاث:
    - عادلة
    - تحتاج تفاوض
    - غير عادلة

    اكتب لي النتيجة بدقة شديدة وبصيغة ثابتة كالتالي:

    البند الأول: [عنوان البند]
    تصنيف: [عادلة / تحتاج تفاوض / غير عادلة]
    توضيح: [توضيح مختصر في سطر واحد فقط]

    البند الثاني: [عنوان البند]
    تصنيف: [عادلة / تحتاج تفاوض / غير عادلة]
    توضيح: [توضيح مختصر في سطر واحد فقط]

    ... وهكذا لكل بند.

    لا تضف أي نص خارج هذا النمط، ولا تستخدم أي علامات ترقيم إضافية أو جمل تفسيرية أخرى.

    النص لتحليله:
    {extracted_text}
    """

    chatgpt_response = classify(prompt)
    return jsonify({'response': chatgpt_response})


if __name__ == '__main__':
    app.run(debug=False, use_reloader=False)

