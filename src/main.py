import re


file = open("../input/raw-text.txt")
text_content = file.read()
line = text_content.strip()


def get_emails_addressess(text_content):
    """
    Extract from the text emails who are in the correct format
    """
    pattern = r"[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    return re.findall(pattern, text_content) 


def get_time_in_hours(text_content):
    """
    Extract from the text time in the correct format HH:MM
    """
    pattern = r"[0-9]{2}:[0-9]{2}(?:\ [AP]M)?"
    return re.findall(pattern,text_content)

def extract_phone_numbers(text_content):
    """
    Extract from the text phone numbers who are in the correct format 
    """
    pattern = r"\+?[0-9]{1,3}(?:[\s\-\(\)]*[0-9]+)+"
    return re.findall(pattern,text_content)

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
    return re.findall(pattern, text_content)
    


if __name__ == "__main__":
    print(get_emails_addressess(text_content))
    print(get_time_in_hours(text_content))
    print(extract_phone_numbers(text_content))
    print(extract_url(text_content))
    print(get_credit_card_numbers(text_content))

