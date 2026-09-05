import requests
import random
import string
from datetime import datetime



def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def generate_phone():
    digits = ''.join(random.choices(string.digits, k=10))
    return f"+7 {digits[0:3]} {digits[3:6]} {digits[6:8]} {digits[8:10]}"


def generate_address():
    streets = [
        "Lenina", "Pushkina", "Gorkogo", "Sovetskaya"
    ]
    street = random.choice(streets)
    apt = random.randint(1, 300)
    return f"{street} St., {apt} apt."

def get_today_date():
    
    return datetime.now().strftime("%Y-%m-%d")



