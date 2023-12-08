import string
import random

def gen_pass(pass_length):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    characters = letters + digits + special
    pwd = ""
    for i in range(pass_length):
        pwd += random.choice(characters)
        
    return pwd
