import re
sentence = "Python is a powerful programming language"
keyword = "python"

if re.search(keyword, sentence, re.IGNORECASE):
    print("Keyword Found")
else:
    print("Keyword Not Found")