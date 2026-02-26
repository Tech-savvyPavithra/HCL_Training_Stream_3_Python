try:
    import non_existent_module   # This module does not exist

except ModuleNotFoundError:
    print("Module not found! Switching to fallback option...")

    # Fallback mechanism
    import math   # Using a built-in module instead
    print("Using math module as fallback.")
    print("Square root of 25 is:", math.sqrt(25))

else:
    print("Module imported successfully!")

finally:
    print("Program finished.")