class InvalidEmailError(Exception):
    pass

def validate_email(email):
    if "@" not in email:
        raise InvalidEmailError("Must contain '@'.")
    return f"Email '{email}' is valid."

email=input("Enter an email address: ")

try:
    print(validate_email(email))
except InvalidEmailError as e:
    print("Error:", e)
else:
    print("Email validation successful.")
finally:    
    print("Email validation process completed.")
    