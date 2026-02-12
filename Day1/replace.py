def replace(text):
    for ch in text:
        if ch.isdigit(): 
            text=text.replace(ch,'#')
    return text
text=input("Enter a string: ")
print(replace(text))