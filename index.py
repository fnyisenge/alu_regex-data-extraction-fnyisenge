import re
import json

with open("sample_input.txt", "r") as file:
    raw_text = file.read()

email_regex = r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b"
url_regex = r"\bhttps?:\/\/[^\s]+\b"
phone_regex = r"\b(\(\d{3}\)\s?\d{3}-\d{3}|\d{3}-\d{3}-\d{3})\b"
time_regex = r"\b((?:[01]?\d|2[0-3]):[0-5]\d|(?:1[0-2]|[1-9]):[0-5]\d\s?(?:AM|PM))\b"
hashtag_regex = r"#[a-zA-Z0-9_]+"
credit_card_regex = r"\b(?:\d{4}[- ]?){3}\d{4}\b"

def safe_extract(pattern, text):
    return re.findall(pattern, text)

def mask_card(card):
    return re.sub(r"\d(?=\d{4})", "*", card)

extracted_data = {
    "emails": safe_extract(email_regex, raw_text),
    "urls": safe_extract(url_regex, raw_text),
    "phone_numbers": safe_extract(phone_regex, raw_text),
    "times": safe_extract(time_regex, raw_text),
    "hashtags": safe_extract(hashtag_regex, raw_text),
    "credit_cards": [mask_card(card) for card in safe_extract(credit_card_regex, raw_text)]
}

print(json.dumps(extracted_data, indent=2))

with open("sample_output.json", "w") as outfile:
    json.dump(extracted_data, outfile, indent=2)
