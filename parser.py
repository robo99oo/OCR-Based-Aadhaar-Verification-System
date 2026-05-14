import re


def extract_details(text):
    cleaned_text = text.replace("\n", " ")
    cleaned_text = re.sub(r"\s+", " ", cleaned_text)

    aadhaar_match = re.search(r"\b\d{4}\s?\d{4}\s?\d{4}\b", cleaned_text)
    dob_match = re.search(r"\b\d{2}/\d{2}/\d{4}\b", cleaned_text)
    gender_match = re.search(r"\b(Male|Female)\b", cleaned_text, re.IGNORECASE)
    pincode_match = re.search(r"\b[1-9][0-9]{5}\b", cleaned_text)

    aadhaar_number = None
    masked_aadhaar = None

    if aadhaar_match:
        aadhaar_number = re.sub(r"\D", "", aadhaar_match.group())
        masked_aadhaar = "XXXX XXXX " + aadhaar_number[-4:]

    return {
        "aadhaar_number": aadhaar_number,
        "masked_aadhaar": masked_aadhaar,
        "dob": dob_match.group() if dob_match else None,
        "gender": gender_match.group().title() if gender_match else None,
        "pincode": pincode_match.group() if pincode_match else None,
    }