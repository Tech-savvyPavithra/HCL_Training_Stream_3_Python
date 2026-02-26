try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print(f"The result is {result}")

except ZeroDivisionError:
    with open("Day11/error_log.txt", "a") as f:
        f.write("Error: Cannot divide by zero!\n")
    print("Something went wrong. Check error_log.txt")

except ValueError:
    with open("Day11/error_log.txt", "a") as f:
        f.write("Error: Invalid number entered!\n")
    print("Something went wrong. Check error_log.txt")

else:
    print("Division successful!")

finally:
    print("Program finished.")