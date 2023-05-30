import re
from typing import Optional

def get_number(string: str) -> Optional[str]:
    numbers = re.findall(r'\d+', string.split(',')[0])
    if not numbers:
        return
    phone = ''.join(numbers)
    if phone[0] == '8':
        phone = '7' + phone[1:]
    elif phone[0] == '7':
        phone = '+' + phone
    elif phone[0] == '9':
        phone = '+7' + phone
    return phone