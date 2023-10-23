import re


# Function to check if a phone number is valid without using Regular Expressions
def isphonenumber(numStr):
    # Check if the length is not equal to 12 (e.g., '123-456-7890')
    if len(numStr) != 12:
        return False

    # Iterate through the characters in the phone number
    for i in range(len(numStr)):
        # Check if the character at index 3 or 7 is not a hyphen
        if i == 3 or i == 7:
            if numStr[i] != "-":
                return False
        else:
            # Check if all other characters are digits
            if not numStr[i].isdigit():
                return False

    # If all checks pass, the phone number is valid
    return True


# Function to check if a phone number is valid using Regular Expressions
def chkphonenumber(numStr):
    # Define a Regular Expression pattern for a valid phone number
    ph_no_pattern = re.compile(r'^\d{3}-\d{3}-\d{4}$')

    # Use the match() function to check if the input matches the pattern
    if ph_no_pattern.match(numStr):
        return True
    else:
        return False


# Input: Ask the user to enter a phone number
ph_num = input("Enter a phone number : ")

# Check without Regular Expressions
print("Without using Regular Expression")
if isphonenumber(ph_num):
    print("Valid phone number")
else:
    print("Invalid phone number")

# Check using Regular Expressions
print("Using Regular Expression")
if chkphonenumber(ph_num):
    print("Valid phone number")
else:
    print("Invalid phone number")
