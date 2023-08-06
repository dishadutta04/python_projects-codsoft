import string
import random

def generate_password(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

if __name__ == "__main__":
    print("Welcome to the Password Generator. Created by T\n")
    service_name = input("Enter the site for your password: ")
    password_length = int(input("Enter your password length: "))
    
    password = generate_password(password_length)
    
    with open("passfile.txt", "a") as file:
        file.write(f"\n{service_name}: {password}")
    
    print("\nPassword has been saved in the file.")
    print("Thank you for using this program.")
