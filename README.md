# Regex Data Extraction & Secure Validation

# Overview
This project extracts structured data from raw text using Python and regular expressions (regex). It validates input to ensure it is well-formed and ignores unsafe or malformed data. The program handles realistic data formats and protects sensitive information.

# Features
- Extracts:
  - Email addresses
  - URLs (HTTP/HTTPS)
  - Phone numbers
  - Time values (12-hour and 24-hour formats)
  - Hashtags
  - Credit card numbers (masked for security)
- Ignores invalid or unsafe input
- Outputs structured JSON

# Project Structure

# Usage
1. Open a terminal and navigate to the `src` folder:
2. Run the script:
3. Extracted data is printed to the console and saved to `output/sample_output.json`.

# Security Considerations
- Only valid emails, URLs, and phone numbers are extracted
- Credit card numbers are masked to prevent exposure
- Malicious input (e.g., `javascript:` URLs) is ignored

# Author
Junior Frontend Developer  
African Leadership University
