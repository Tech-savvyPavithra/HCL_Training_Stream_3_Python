def case(text):
    text=set(text.strip().lower().split())
    return " ".join(sorted(text))

text =input("Enter a sentence: ")
print(case(text))