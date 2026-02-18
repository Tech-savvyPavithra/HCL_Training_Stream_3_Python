def check_strength(pwd, min_len=8):
    result = {
        "length_ok": len(pwd) >= min_len,
        "has_upper": False,
        "has_lower": False,
        "has_digit": False,
        "has_special": False
    }

    for ch in pwd:
        if ch.isupper():
            result["has_upper"] = True
        elif ch.islower():
            result["has_lower"] = True
        elif ch.isdigit():
            result["has_digit"] = True
        elif not ch.isalnum():   
            result["has_special"] = True

    result["score"] = sum(result.values())
    return result

password = input("Enter a password to check: ")
strength = check_strength(password) 
print(f"Password strength: {strength['score']}/5")
print(f"Details: {strength}")