import pdfplumber

def parse_pdf_transaction(file_path):
    transactions = []
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            transactions.append(text)  # For now, just save raw text
    return transactions