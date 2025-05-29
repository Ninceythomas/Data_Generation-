import importlib

# Load the standard library random module, ignoring the local random.py file
stdlib_random = importlib.import_module('random')

import string
from faker import Faker

fake = Faker()

def random_name(prefix="X", length=6):
    return prefix + ''.join(stdlib_random.choices(string.ascii_uppercase, k=length))

def random_number(min_value=1, max_value=100):
    return stdlib_random.randint(min_value, max_value)

def random_person_name():
    return fake.name()

def random_company_name():
    return fake.company()
