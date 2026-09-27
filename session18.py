# 1
import re

text = """
Call me at 9876543210 or 8123456789.
Price is 500 and order number is 1234567890.
Another number is 7654321098.
"""

pattern = r'\b[789]\d{9}\b'

numbers = re.findall(pattern, text)

print(numbers)


# 2

import re

def check_date(text):
    pattern = r'\b\d{2}/\d{2}/\d{4}\b'

    if re.search(pattern, text):
        return True
    else:
        return False


print(check_date("My birthday is 25/06/2024"))
print(check_date("Today is a good day"))


# 3
import re

text = """
Contact us at rahul@gmail.com or support@zomato.com.
Another email is user123@yahoo.com.
"""

pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'

emails = re.findall(pattern, text)

print(emails)

# 4
import re

text = "My phone number is 9876543210."

masked_text = re.sub(r'\b\d{10}\b', lambda m: "******" + m.group()[-4:], text)

print(masked_text)

# 5

import re

order1 = "Your order ID is OD123456789012345000"
order2 = "Order ID: AB123456789012345000"

pattern = r'\bOD\d{18}\b'

result1 = re.search(pattern, order1)
result2 = re.search(pattern, order2)

print(bool(result1))
print(bool(result2))