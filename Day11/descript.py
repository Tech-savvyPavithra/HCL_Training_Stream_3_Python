import csv

file_path = "Day11/items.csv"

with open(file_path, "r") as f:
    reader = csv.DictReader(f)
    
    for row in reader:
        price = float(row["price"])   # Convert price to number
        
        if price > 50:
            print("Description:", row["description"])