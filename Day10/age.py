def check(age):
    if age<18:
        raise ValueError("Age cannot be less than 18")
    else:
        return f"Age is {age}"
    
age = int(input("Enter your age: "))

try:
    print(check(age))
except ValueError as e:
    print("Error:", e)
else:
    print("You are above 18.")
finally:
    print("Age check completed.")
    