numbers = [25, 0, 5, 10, 0, 20]

for num in numbers:
    try:
        result = 100 / num
    except ZeroDivisionError:
        print(f"Cannot divide by zero for number {num}!")
    else:
        print(f"100 divided by {num} is {result}")
    finally:
        print(f"Finished processing number {num}.")