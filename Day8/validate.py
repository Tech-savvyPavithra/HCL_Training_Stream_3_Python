from abc import ABC, abstractmethod
import re

class Validator(ABC):

    @abstractmethod
    def validate(self, data):
        pass

class EmailValidator(Validator):

    def validate(self, data):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if re.match(pattern, data):
            return "Valid Email"
        return "Invalid Email"

class PasswordValidator(Validator):

    def validate(self, data):
        if (len(data) >= 8 and
            any(c.isupper() for c in data) and
            any(c.islower() for c in data) and
            any(c.isdigit() for c in data)):
            return "Strong Password"
        return "Weak Password"

email = EmailValidator()
password = PasswordValidator()

print(email.validate("test@example.com"))
print(password.validate("Pass1234"))