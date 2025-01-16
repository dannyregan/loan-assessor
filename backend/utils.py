import pdfplumber
import pytesseract
from PIL import Image


def parse_pdf_transaction(file_path):
    data = {"text": [], "tables": []}

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            # Extract raw text
            text = page.extract_text()
            if text:
                lines = text.split('\n')
                for line in lines:
                    if line.strip():
                        data["text"].append({"raw_line": line})
                # data["text"].append(text)

            # Extract tables
            # table = page.extract_table()
            # if table:
            #     data["tables"].append(table)

    return data
    # transactions = []
    # with pdfplumber.open(file_path) as pdf:
    #     for page in pdf.pages:
    #         lines = page.extract_text().split('\n')
    #         for line in lines:
    #             # Example: Split text into date, description, and amount
    #             if line.strip():  # Skip empty lines
    #                 transactions.append({"raw_line": line})
    #         # text = page.extract_text()
    #         # transactions.append(text)  # For now, just save raw text
    # return transactions


def identify_bank(text_array):
    for item in text_array:
        if "idfc first bank" in item["raw_line"].lower():
            return "IDFC First Bank"
        if "lloyds bank" in item["raw_line"].lower():
            return "Lloyds Bank"
        if "usbank" in item["raw_line"].lower():
            return "US Bank"
        if "commbank" in item["raw_line"].lower():
            return "Commonwealth Bank"
    return False

def parse_pdf_OCR(file_path):
    image = Image.open(file_path)
    text = pytesseract.image_to_string(image)
    print("Extracted Text:")
    print(text)

# def organize_data(data):
#     organized_data = {
        
#     }

#     return organized_data