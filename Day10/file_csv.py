import csv
import os

# Create the folder "Day10" if it doesn't exist
folder_path = "Day10"
os.makedirs(folder_path, exist_ok=True)

books = [
    {"title": "Python Basics", "author": "John Smith", "price": 450},
    {"title": "Data Science Intro", "author": "Alice Brown", "price": 550},
    {"title": "AI Fundamentals", "author": "David Lee", "price": 650}
]

# Path to save the CSV inside "Day10" folder
file_path = os.path.join(folder_path, "books.csv")

with open(file_path, "w", newline="") as f:
    fieldnames = ["title", "author", "price"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    
    writer.writeheader()     # Write column headers
    writer.writerows(books)  # Write multiple rows

print(f"Books written to CSV successfully at {file_path}!")