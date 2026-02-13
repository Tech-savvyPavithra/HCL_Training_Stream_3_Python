def countsubstring(s, sub):
    count = 0
    for i in range(len(s) - len(sub) + 1):
        if s[i:i+len(sub)] == sub:
            count += 1
    return count

s = input("Enter a sentence: ")
sub = input("Enter a substring: ")

count = countsubstring(s, sub)
print(f"The '{sub}' appears {count} times in the sentence.")
