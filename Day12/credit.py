import re
card = "1234 5678 9012 3456"
pattern = re.sub(r"\d{4}\s\d{4}\s\d{4}", "**** **** ****", card)
print(pattern)