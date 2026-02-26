import json

file_path = "Day10/data.json"

try:
    with open(file_path, "r") as f:
        content = f.read()
    
    data = json.loads(content)
    
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found!")

except json.JSONDecodeError:
    print(f"Error: The file '{file_path}' does not contain valid JSON!")

else:
    print("JSON data successfully loaded!")
    print(data)

finally:
    print("Program finished.")