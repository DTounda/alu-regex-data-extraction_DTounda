import re
import json


def valide_inputs(content):
    """
    It check for null bytes and extremely long lines 
    that could indicate a buffer manipulation attempt or malformed data
    """
    content = content.replace("\x00", "")
    line = content.splitlines()
    for text in line:
        line = line[:2000]
    return "\n".join(line)


def get_emails_addressess(text_content):
    """
    Extract from the text emails who are in the correct format
    meaning it reject emails longer than 254 characters
    """
    pattern = r"[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    found = re.findall(pattern, text_content)
    emails_addressess = []
    for emails in found:
        if len(emails) <= 254:
            emails_addressess.append(emails)
    return emails_addressess


def valide_alu_emails(text_content):
    """
    Extract from the text emails that respect the pattern of ALU emails
    """
    emails = get_emails_addressess(text_content)

    alu_si       = r"^[a-zA-Z0-9._-]+@si\.alueducation\.com$"
    alu_official = r"^[a-zA-Z0-9._-]+@alueducation\.com$"
    alu_alumni   = r"^[a-zA-Z0-9._-]+@alumni\.alueducation\.com$"

    result = {
        "alu_official": [],
        "alu_alumni":   [],
        "alu_si":       [],
        "non_alu":      []
    }

    for email in emails:
        if re.fullmatch(alu_si, email):
            result["alu_si"].append(email)
        elif re.fullmatch(alu_alumni, email):
            result["alu_alumni"].append(email)
        elif re.fullmatch(alu_official, email):
            result["alu_official"].append(email)
        else:
            result["non_alu"].append(email)

    return result


def get_time_in_hours(text_content):
    """
    Extract from the text time in the correct format HH:MM
    """
    pattern = r"[0-9]{2}:[0-9]{2}(?:\ [AaPp]M)?"
    return re.findall(pattern, text_content)


def extract_phone_numbers(text_content):
    """
    Extract from the text phone numbers who are in the correct format
    """
    pattern = r"(?:\+|0)[0-9]{1,3}(?:[\s\-\(\)]*[0-9]+)+"
    found = re.findall(pattern, text_content)
    match = []
    for number in found:
        digits_only = re.sub(r"\D", "", number)
        if 7 <= len(digits_only) <= 15:
            match.append(number.strip())
    return match


def extract_url(text_content):
    """
    Extract from the text url in the correct format
    """
    pattern = r"https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}[/\w\-.?&#%=]*"
    return re.findall(pattern, text_content)


def get_credit_card_numbers(text_content):
    """
    Extract from the text credit card number who are in the correct format
    """
    pattern = r"\b(?:\d{4}[\s\-]?){3}\d{4}\b"
    found = re.findall(pattern, text_content)
    matches = []
    for credit_card in found:
        numbers = re.sub(r"\D", "", credit_card)
        if len(numbers) == 16:
            matches.append("**** **** **** " + numbers[-4:])
        elif len(numbers) == 15:
            matches.append("**** ****** *" + numbers[-4:])
    return matches


try:
    file = open("../input/raw-text.txt")
    text_content = file.read()
    text_content = valide_inputs(text_content)
except FileNotFoundError:
    print("! The input file was not found.")
    exit(1)



if __name__ == "__main__":
    all_emails   = get_emails_addressess(text_content)
    alu_emails   = valide_alu_emails(text_content)
    times        = get_time_in_hours(text_content)
    phones       = extract_phone_numbers(text_content)
    urls         = extract_url(text_content)
    credit_cards = get_credit_card_numbers(text_content)

    output = {
        "emails": {
            "alu_official": alu_emails["alu_official"],
            "alu_alumni":   alu_emails["alu_alumni"],
            "alu_si":       alu_emails["alu_si"],
            "non_alu":      alu_emails["non_alu"]
        },
        "times":         times,
        "phone_numbers": phones,
        "urls":          urls,
        "credit_cards":  credit_cards
    }

    print(json.dumps(output, indent=2))
