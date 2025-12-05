import re

def is_valid_email(email: str) -> bool:
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def is_strong_password(password: str) -> bool: # This will take the password as string and return a boolean value
    return len(password) >= 6