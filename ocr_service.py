import cv2
import numpy as np
import pytesseract
from pyzbar.pyzbar import decode

# Windows users: uncomment and set your Tesseract path
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


class OCRService:

    def preprocess_image(self, image_path):
        image = cv2.imread(image_path)

        if image is None:
            raise ValueError("Could not read image")

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        gray = cv2.resize(
            gray,
            None,
            fx=1.5,
            fy=1.5,
            interpolation=cv2.INTER_CUBIC
        )

        denoised = cv2.fastNlMeansDenoising(gray, None, 30, 7, 21)

        threshold = cv2.adaptiveThreshold(
            denoised,
            255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            31,
            2
        )

        return threshold

    def extract_text(self, image):
        config = "--oem 3 --psm 6"
        text = pytesseract.image_to_string(image, lang="eng", config=config)
        return text

    def detect_qr(self, image_path):
        image = cv2.imread(image_path)
        qr_data = []

        decoded_objects = decode(image)

        for obj in decoded_objects:
            try:
                qr_data.append(obj.data.decode("utf-8"))
            except Exception:
                qr_data.append(str(obj.data))

        return qr_data