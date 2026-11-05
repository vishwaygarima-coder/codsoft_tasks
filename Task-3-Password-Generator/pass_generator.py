import random
import string

print("==== PASSWORD GENERATOR ====")

length = int(input("Enter password length: "))

if length <= 0:
    print("Please enter a valid length.")
    
else:
    characters = string.ascii_letters + string.digits + string.punctuation
    
    password = ""
    
    for i in range(length):
        password += random.choice(characters)
        
    print("Your Generated Password is:", password)
