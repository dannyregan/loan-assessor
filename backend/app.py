# from flask import Flask, request, jsonify # Create and manage the web app, access incoming data from frontend, jsonify
# import os # interact with computer software (create folders)

# from utils import parse_pdf_transaction
# from utils import identify_bank
# from utils import parse_pdf_OCR

# app = Flask(__name__)

# UPLOAD_FOLDER = 'uploads'
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# @app.route('/')
# def home():
#     return "Welcome to the Loan Assessor API by Danny Regan."

# @app.route('/parse-pdf', methods=['POST'])
# def parse_pdf():
#     if 'file' not in request.files:
#         return jsonify({"error": "No file provided"}), 400
    
#     file = request.files['file']

#     if file.filename == '':
#         return jsonify({"error": "No selected file"}), 400

#     file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
#     file.save(file_path)

#     parse_pdf_OCR(file_path)

#     # line_by_line_data = parse_pdf_transaction(file_path)
#     # text_array = line_by_line_data["text"]

#     # print(line_by_line_data["text"][:10])

#     # bank = identify_bank(text_array)
#     # print(bank)


#     return jsonify({
#     "file_name": file.filename
#     # "parsed_data": line_by_line_data
# })


# if __name__ == '__main__':
#     app.run(debug=True)