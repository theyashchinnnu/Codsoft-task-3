import random
import string

def generate_password(length):
    # Define the characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a password by randomly choosing characters from the defined set
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

# Example: Generate a 12-character password
password = generate_password(12)
print("Generated Password:", password)
