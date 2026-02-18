def normalize_name(s):
    s = s.strip()
    if not s:
        return ""
    words = s.split()
    return " ".join(words).title()

sent = input("Enter your name: ")
normalized_sent = normalize_name(sent)
print("Normalized name:", normalized_sent)
   