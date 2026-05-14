from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

import pytesseract
from PIL import Image

import shutil
import os
import cv2
import numpy as np
import easyocr

from parser import extract_details

app = FastAPI(title="Aadhaar OCR Verification API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Tesseract Path
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

reader = easyocr.Reader(['en'])

@app.get("/")
def home():
    return {"message": "API Running Successfully"}


@app.post("/verify-aadhaar")
async def verify_aadhaar(file: UploadFile = File(...)):

    # Save uploaded file
    file_path = f"temp_{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Read image using OpenCV
    image = cv2.imread(file_path)

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Resize image
    gray = cv2.resize(
        gray,
        None,
        fx=2,
        fy=2,
        interpolation=cv2.INTER_CUBIC
    )

    # Remove noise
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    # Thresholding
    gray = cv2.threshold(
        gray,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )[1]

    #OCR Extraction
    results = reader.readtext(gray)

    text = " ".join([result[1] for result in results])
    # Extract Aadhaar Details
    extracted_details = extract_details(text)

    # Delete temporary file
    os.remove(file_path)

    return {
        "filename": file.filename,
        "ocr_text": text,
        "extracted_details": extracted_details
    }