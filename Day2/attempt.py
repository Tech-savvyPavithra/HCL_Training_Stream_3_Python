def check_password(correct):
    attempts = 3
    for i in range(attempts):
        entered = input("Enter password: ")
        if entered == correct:
            return "Unlocked"
    return "Locked"


print(check_password("python123"))
