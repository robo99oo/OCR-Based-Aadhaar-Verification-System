# 🚀 OCR-Based Aadhaar Verification System

An AI-powered OCR verification system built using FastAPI, OpenCV, and Tesseract OCR to automate Aadhaar detail extraction from document images.

This project simulates a real-world KYC verification workflow used in banking and fintech systems by combining OCR extraction, image preprocessing, structured parsing, and secure Aadhaar masking.

---

# 📌 Project Overview

Traditional KYC verification processes often involve manual document inspection and repetitive data entry, which can be time-consuming and error-prone.

This project aims to simplify Aadhaar verification workflows by automatically extracting key identity details from uploaded Aadhaar images using OCR and Computer Vision techniques.

The system preprocesses uploaded images, extracts text using Tesseract OCR, identifies important fields such as Aadhaar number and DOB, masks sensitive information, and returns structured API responses using FastAPI.

---

# ✨ Features

✅ Aadhaar OCR Extraction using Tesseract OCR
✅ OpenCV-based image preprocessing
✅ Structured field extraction
✅ Aadhaar masking for privacy/security
✅ FastAPI backend APIs
✅ Swagger API Testing Interface
✅ Real-time JSON response generation

---

# 🧠 Workflow Architecture

```text
User Uploads Aadhaar Image
            ↓
FastAPI Receives Image
            ↓
OpenCV Image Preprocessing
(Grayscale + Resize + Thresholding)
            ↓
Tesseract OCR Text Extraction
            ↓
Regex-Based Field Parsing
            ↓
Aadhaar Masking
            ↓
Structured JSON Response
```

---

# 🛠 Tech Stack

| Technology    | Purpose                     |
| ------------- | --------------------------- |
| Python        | Core Programming Language   |
| FastAPI       | Backend API Framework       |
| OpenCV        | Image Processing            |
| Tesseract OCR | Text Extraction             |
| Regex Parsing | Structured Field Extraction |
| Swagger UI    | API Testing                 |

---

# 📂 Project Structure

```text
OCR-Based-Aadhaar-Verification-System/
│
├── main.py
├── parser.py
├── ocr_service.py
├── run.py
├── requirements.txt
├── simple_test.py
└── README.md
```

---

# ⚡ API Endpoint

## Verify Aadhaar

```http
POST /verify-aadhaar
```

### Request

Upload Aadhaar image file.

### Response Example

```json
{
  "filename": "aadhaar.jpg",
  "ocr_text": "Government of India...",
  "extracted_details": {
    "aadhaar_number": "123456789012",
    "masked_aadhaar": "XXXX XXXX 9012",
    "dob": "03/09/2000",
    "gender": "Female",
    "pincode": "250001"
  }
}
```

## Project Workflow Diagram

<img width="1000" height="956" alt="image" src="https://github.com/user-attachments/assets/d5c75d34-b72a-4e1c-9cd0-f545bc92c5b9" />


---

# ▶️ How To Run Locally

## 1. Clone Repository

```bash
git clone https://github.com/robo99oo/OCR-Based-Aadhaar-Verification-System.git
```

## 2. Navigate To Project

```bash
cd OCR-Based-Aadhaar-Verification-System
```

## 3. Create Virtual Environment

```bash
python -m venv .venv
```

## 4. Activate Virtual Environment

### Windows

```bash
.venv\Scripts\activate
```

---

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 6. Run Application

```bash
python run.py
```

---

## 7. Open Swagger Docs

```text
http://127.0.0.1:8000/docs
```

---

# 🔮 Future Enhancements

🔹 Fraud & Blur Detection
🔹 Voice-Assisted Consent Verification
🔹 Face Verification
🔹 Risk Scoring Engine
🔹 PAN Card Support
🔹 AI-Powered Smart KYC Workflow

---

# 💡 Learning Outcomes

Through this project, I explored:

* OCR pipelines using Tesseract OCR
* OpenCV preprocessing techniques
* FastAPI backend development
* Structured data extraction using regex
* API-based document verification workflows
* Real-world AI-assisted KYC system design

---

# 👩‍💻 Author

## Kshiti Tyagi

Data Analyst | GenAI / AI / ML Engineer | FastAPI | RAG | OCR | Computer Vision

🔗 LinkedIn: [https://www.linkedin.com/in/kshiti-tyagi/](https://www.linkedin.com/in/kshiti-tyagi/)

🔗 GitHub: [https://github.com/robo99oo](https://github.com/robo99oo)

---

# ⭐ If you found this project interesting, consider giving it a star!
