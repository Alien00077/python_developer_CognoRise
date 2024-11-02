import random
import string

def password_generator(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    print("Generated Password:", password)

length = int(input("Enter the length of the password: "))
password_generator(length)
