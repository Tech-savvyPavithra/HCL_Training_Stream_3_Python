word = "ERROR"

with open("Day10/log.txt", "r") as f:
    content = f.read().upper()
    count = content.count(word.upper())

print("ERROR appears", count, "times")