def smart(sent):
    words = sent.split()
    result = []
    for word in words:
        if word.upper() in ["AI", "ML", "NLP", "API", "CPU", "SQL", "HTML", "CSS"]:
            result.append(word.upper())
        else:
            result.append(word.capitalize())
    return ' '.join(result)

str=input("Enter a sentence: ")
print(smart(str))