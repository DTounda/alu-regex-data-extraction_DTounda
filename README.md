# ALU Regex Data Extraction

A Python utility that scans raw text files and extracts structured data using regular expressions. Built for the African Leadership University context, it classifies emails by domain type, validates phone numbers and credit cards, and outputs clean JSON.

---

## Features

- **Email extraction & classification** — separates ALU official, ALU alumni, ALU Student Institute (SI), and non-ALU emails
- **Time extraction** — matches both 24-hour (`14:32`) and 12-hour (`03:47 AM`) formats
- **Phone number extraction** — handles international formats with country codes, spaces, and dashes; enforces 7–15 digit length
- **URL extraction** — captures `http` and `https` URLs including query strings and fragments
- **Credit card masking** — detects 16-digit card numbers and masks all but the last 4 digits

---

## Project Structure

alu-regex-data-extraction_DTounda/
├── input/
│   └── raw-text.txt        # Input file to scan
└── src/
└── main.py             # Main extraction script

## Getting Started

### Prerequisites

- Python 3.7+
- No external dependencies — uses only the Python standard library (`re`, `json`)

### Running the script

```bash
cd src
python main.py
```

The script reads from `../input/raw-text.txt` and prints the extracted data as formatted JSON to stdout.

---

## Output Format

```json
{
  "emails": {
    "alu_official": ["admin@alueducation.com"],
    "alu_alumni":   ["a.diallo@alumni.alueducation.com"],
    "alu_si":       ["academics@si.alueducation.com"],
    "non_alu":      ["j.okafor@gmail.com"]
  },
  "times":         ["14:32", "03:47 AM"],
  "phone_numbers": ["+250 788 123 456", "0788-456-789"],
  "urls":          ["https://portal.alueducation.com/login"],
  "credit_cards":  ["**** **** **** 1111"]
}
```

---

## How It Works

### Input Sanitisation
Strips null bytes and truncates lines longer than 2000 characters to guard against malformed or adversarial input.

### Email Extraction & Classification
Matches the standard email format and rejects any address over 254 characters (the RFC 5321 maximum). Emails are then classified into four buckets:

| Category | Pattern |
|---|---|
| `alu_official` | `*@alueducation.com` |
| `alu_alumni` | `*@alumni.alueducation.com` |
| `alu_si` | `*@si.alueducation.com` |
| `non_alu` | Everything else |

### Time Extraction
Matches `HH:MM` with an optional `AM`/`PM` suffix (case-insensitive).

### Phone Number Extraction
Matches strings starting with `+` or `0` followed by digits, spaces, dashes, and parentheses. Post-match filtering enforces the E.164 digit range of 7–15 digits.

### URL Extraction
Matches `http://` and `https://` URLs, capturing paths, query parameters, and anchors.

### Credit Card Masking
Detects 16-digit sequences (with optional spaces or dashes), then replaces the first 12 digits with `**** **** ****` — only the last 4 digits are ever shown.

---

## Security Considerations

- Input is sanitised before processing to remove null bytes and cap line length
- Credit card numbers are never stored or printed in full — only the last 4 digits are shown
- The extractor is read-only; it does not modify or delete the input file

---

## Author

**Dorcase Lesly Nana Tounda**
BSc Software Engineering — African Leadership University
[github.com/DTounda](https://github.com/DTounda)
