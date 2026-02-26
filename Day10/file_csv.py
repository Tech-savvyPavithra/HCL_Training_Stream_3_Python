import csv

books = [
    {"title": "Python Basics", "author": "John Smith", "price": 450},
    {"title": "Data Science Intro", "author": "Alice Brown", "price": 550},
    {"title": "AI Fundamentals", "author": "David Lee", "price": 650}
]

file_path = "Day10/books.csv"

with open(file_path, "w", newline="") as f:
    
    fieldnames = ["title", "author", "price"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(books)

print(f"Books have been written to '{file_path}' successfully!")