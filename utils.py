import re

def clean_text(raw_text):
    """
    Cleans and preprocesses raw text.

    Args:
        raw_text (str): The unprocessed text.

    Returns:
        str: The cleaned and structured text.
    """
    # Remove extra whitespace and newlines
    cleaned_text = re.sub(r'\s+', ' ', raw_text).strip()
    
    # Remove non-ASCII characters
    cleaned_text = re.sub(r'[^\x00-\x7F]+', ' ', cleaned_text)
    
    # Remove unnecessary symbols or formatting artifacts
    cleaned_text = re.sub(r'[\u2022\u2023\u25E6\u2024\u2219]', '', cleaned_text)  # Common bullet symbols
    cleaned_text = re.sub(r'[^\w\s.,!?\'"-]', '', cleaned_text)  # Non-alphanumeric symbols
    
    # Standardize spaces around punctuation
    cleaned_text = re.sub(r'\s+([.,!?])', r'\1', cleaned_text)
    cleaned_text = re.sub(r'([.,!?])\s+', r'\1 ', cleaned_text)
    
    # Convert to lowercase (optional, depending on the use case)
    cleaned_text = cleaned_text.lower()
    
    return cleaned_text
