# User Inputs their password
userEntry = input("Enter your password: ")

# Saved Password on record
savedPassword = "myPasscode2024/"

# System checks if password is valid.
if userEntry == savedPassword:
    print("Access Granted")
else :
    print("Access Denied")