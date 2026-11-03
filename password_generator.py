
import secrets
import string

def generate_password(length):
    if length < 4:
        print("Password length must be at least 4!")
        return

    # Character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    # Ensure at least one character from each category
    password = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(special)
    ]

    # Combine all characters
    all_characters = lowercase + uppercase + digits + special

    # Generate remaining characters
    for i in range(length - 4):
        password.append(secrets.choice(all_characters))

    # Shuffle password characters
    secrets.SystemRandom().shuffle(password)

    return ''.join(password)


# Main program
print("================================")
print("      PASSWORD GENERATOR")
print("================================")

while True:
    try:
        length = int(input("\nEnter password length (minimum 4): "))

        if length < 4:
            print("Please enter a length of at least 4.")
            continue

        password = generate_password(length)

        print("\nYour generated password is:")
        print(password)

        again = input("\nGenerate another password? (yes/no): ").lower()

        if again != "yes":
            print("\nThank you for using Password Generator!")
            break

    except ValueError:
        print("Please enter a valid number!")
