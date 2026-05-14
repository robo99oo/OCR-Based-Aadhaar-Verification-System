from PIL import Image, ImageDraw, ImageFont
import pytesseract

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

img = Image.new("RGB", (900, 500), "white")
draw = ImageDraw.Draw(img)

text = """
Government of India
Kshiti Tyagi
DOB: 12/08/2000
Female
1234 5678 9012
Address: Meerut, Uttar Pradesh 250001
"""

draw.text((50, 50), text, fill="black")

img.save("dummy_aadhaar.png")

ocr_text = pytesseract.image_to_string(Image.open("dummy_aadhaar.png"))

print("OCR Output:")
print(ocr_text)