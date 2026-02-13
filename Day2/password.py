crt="Python"
max = 3
curr =0
while curr < max:
    password = input("Enter the password: ")
    if password == crt:
        print("Correct password")
        break
    else:
        print("Wrong password")
    curr += 1
    rem = max - curr
    if rem > 0:
        print(f"You have {rem} attempts left")
    else:
        print("No attempts left. Access denied.")