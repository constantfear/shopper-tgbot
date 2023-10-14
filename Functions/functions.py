import re

def is_valid_phone_number(phone_number: str) -> bool:
    """The function checks the correctness of the entered phone number"""
    
    # Remove '+' if it exists
    phone_number = phone_number.replace('+', '')

    # Check that the number contains only digits
    if not re.match(r'^\d+$', phone_number):
        return False
    
    # Check that the number starts with 7 or 8
    if not re.match(r'^[78]', phone_number):
        return False
    
    # Check that the number consists of 11 digits
    if len(phone_number) != 11:
        return False
    
    return True

