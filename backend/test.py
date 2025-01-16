# utils.py
from pdf2image import convert_from_path
import pytesseract
from PIL import Image
import os

def convert_pdf_to_images(pdf_path, output_folder):
    """
    Converts a PDF to images and saves them in the output folder.
    """
    os.makedirs(output_folder, exist_ok=True)
    images = convert_from_path(pdf_path)
    for i, image in enumerate(images):
        image_path = os.path.join(output_folder, f"page_{i + 1}.jpg")
        image.save(image_path, "JPEG")
        print(f"Saved image: {image_path}")

def perform_ocr_on_images(image_folder):
    """
    Performs OCR on images in the given folder and returns extracted text as a list.
    """
    texts = []
    for filename in sorted(os.listdir(image_folder)):
        if filename.endswith(".jpg"):
            image_path = os.path.join(image_folder, filename)
            text = pytesseract.image_to_string(Image.open(image_path))
            pytesseract.ima
            texts.append(text)
    return texts
