import json

with open("Day10/data.json", "r") as f:
    data = json.load(f)   # Convert JSON to Python dictionary

print(data["name"])