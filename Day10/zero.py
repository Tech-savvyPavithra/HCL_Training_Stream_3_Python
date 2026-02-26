try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
    result = num1 / num2

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Please enter a valid number!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print(f"The result of dividing {num1} by {num2} is {result}")
finally:
    print("Program execution completed.")