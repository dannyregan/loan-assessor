from flask import Flask, request, jsonify
import os
from test import convert_pdf_to_images, perform_ocr_on_images

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'output_images'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return "Welcome to the Loan Assessor API."

@app.route('/parse-pdf', methods=['POST'])
def parse_pdf():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if not file.filename.endswith('.pdf'):
        return jsonify({"error": "File is not a PDF"}), 400

    # Save uploaded file
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    # Convert PDF to images
    try:
        convert_pdf_to_images(file_path, OUTPUT_FOLDER)
    except Exception as e:
        return jsonify({"error": f"Failed to process PDF: {str(e)}"}), 500

    # Perform OCR on images
    try:
        texts = perform_ocr_on_images(OUTPUT_FOLDER)
    except Exception as e:
        return jsonify({"error": f"OCR failed: {str(e)}"}), 500

    return jsonify({"texts": texts}), 200

if __name__ == '__main__':
    app.run(debug=True)
