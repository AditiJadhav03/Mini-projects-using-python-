#import random, string

#length = int(input("Enter password length: "))
#chars = string.ascii_letters + string.digits + string.punctuation
#password = "".join(random.choice(chars) for _ in range(length))
#print("Generated Password:", password)

'''this is a way to write simple password generator but lets try to add more in it '''
import random   # Used for random selection of characters
import string   # Provides predefined sets of characters (letters, digits, punctuation)

# Function to generate a strong password
def generate_password(length=12, use_digits=True, use_special=True):
    """
    Generates a random password based on user preferences.
    
    Parameters:
    length (int): The total length of the password (default is 12).
    use_digits (bool): Whether to include numbers (0-9).
    use_special (bool): Whether to include special characters like !, @, #, etc.

    Returns:
    str: A randomly generated secure password.
    """

    # Start with letters (uppercase + lowercase)
    characters = string.ascii_letters  
    # string.ascii_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Add digits if the user wants them
    if use_digits:
        characters += string.digits  
        # string.digits = "0123456789"

    # Add special characters if the user wants them
    if use_special:
        characters += string.punctuation  
        # string.punctuation = !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

    # Ensure the character set is not empty
    if not characters:
        raise ValueError("No character types selected for password!")

    # Generate password by randomly selecting from the character set
    password = ''.join(random.choice(characters) for _ in range(length))
    # ''.join() → joins characters into one string
    # random.choice(characters) → picks a random character from the set
    # for _ in range(length) → repeats this process for "length" times

    return password

# Example usage:
print(" Advanced Password Generator ")

# Take input from user for customization
length = int(input("Enter desired password length (e.g., 12, 16, 20): "))
use_digits = input("Include digits? (y/n): ").lower() == 'y'
use_special = input("Include special characters? (y/n): ").lower() == 'y'

# Generate and show password
new_password = generate_password(length, use_digits, use_special)
print("\n Your secure password is:", new_password)

