old_word = "Java"
new_word = "Python"

with open("Day10/My_file.txt", "r") as f:
    content = f.read()

updated_content = content.replace(old_word, new_word)

with open("Day10/My_file.txt", "w") as f:
    f.write(updated_content)
    
print("Replacement completed successfully!")