import random
import string

# Ask user for password length
length = int(input("Enter the desired password length: "))

# Characters to use: letters, digits, symbols
characters = string.ascii_letters + string.digits + string.punctuation

# Generate password
password = "".join(random.choice(characters) for _ in range(length))

# Display password
print("Generated Password:", password)
