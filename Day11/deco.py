from functools import wraps

def log_call(func):
    @wraps(func)   # Preserves __name__ and __doc__
    def wrapper(*args, **kwargs):
        # Print function name and arguments before running
        print(f"Calling function: {func.__name__}")
        print(f"Arguments: args={args}, kwargs={kwargs}")
        
        # Run the function
        result = func(*args, **kwargs)
        
        # Print return value after running
        print(f"Function returned: {result}")
        
        return result
    return wrapper

@log_call
def add(a, b):
    """Adds two numbers."""
    return a + b

add(5, 3)