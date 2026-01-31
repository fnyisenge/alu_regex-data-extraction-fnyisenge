document.getElementById("extractBtn").addEventListener("click", () => {
    const text = document.getElementById("inputText").value;

    // Regex patterns (realistic & defensive)
    const patterns = {
        emails: /\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}\b/g,
        urls: /\bhttps?:\/\/[^\s<>"]+/gi,
        phones: /\b(\(\d{3}\)\s?|\d{3}[-.])\d{3}[-.]\d{4}\b/g,
        creditCards: /\b(?:\d{4}[- ]?){3}\d{4}\b/g,
        times: /\b([01]?\d|2[0-3]):[0-5]\d(\s?(AM|PM))?\b/gi
    };

    // Extract & sanitize
    const extractSafe = (regex, mask = false) => {
        const matches = text.match(regex) || [];
        return matches.map(item => {
            if (mask) {
                // Mask sensitive data (credit cards)
                return item.replace(/\d(?=\d{4})/g, "*");
            }
            return item;
        });
    };

    const result = {
        emails: extractSafe(patterns.emails),
        urls: extractSafe(patterns.urls),
        phoneNumbers: extractSafe(patterns.phones),
        creditCards: extractSafe(patterns.creditCards, true),
        times: extractSafe(patterns.times)
    };

    document.getElementById("output").textContent =
        JSON.stringify(result, null, 2);
});
