import random
import string

def generate_password(length):
    # Define the character set
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage
password_length = 12
password = generate_password(password_length)
print(password)
