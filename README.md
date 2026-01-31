# Input Description
The application accepts *raw text input*, representing data returned from an external API.  
The text includes realistic formatting such as:
- Emails
- URLs
- Phone numbers
- Credit card numbers
- Time values
- Irregular spacing and mixed content

Malicious or malformed content (e.g., script tags) may also appear in the input.

# Data Types Extracted
The program extracts and validates the following data types:

1. *Email Addresses*
2. *URLs*   
3. *Phone Numbers*
4. *Credit Card Numbers*
   - Output is masked for security
5. *Time (12-hour & 24-hour formats)*

# Security Considerations
- Regex patterns are designed to avoid over-matching unsafe input.
- Sensitive data such as *credit card numbers is masked* before being displayed.
- Extracted content is rendered as *plain text / JSON*, never as HTML.
- Script tags or malicious payloads are ignored and not executed.
- The program assumes all input is untrusted.

#  How to Run the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/fnyisenge/alu_regex-data-extraction-fnyisenge
