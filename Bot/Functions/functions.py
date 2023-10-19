import re
from tabulate import tabulate

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

def to_table_message(table_header: list[str], table_rows) -> str:

    if not table_rows:
        return ""

    table = tabulate(table_rows, table_header, tablefmt="pretty")


    return '<code>'+table+'</code>'

def to_message(data) -> str:
    msg = f"""
Тип: {data[4]}
Название: {data[1]}
Описание: {data[2]}
Цена за единицу товара: {data[3]}

Введите количество
"""
    return msg
