# utils/validators.py
import re

def validate_email(email):
    """Validate email format."""
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def validate_password(password):
    """Validate password strength."""
    # Add your password validation logic here
    return len(password) >= 8
