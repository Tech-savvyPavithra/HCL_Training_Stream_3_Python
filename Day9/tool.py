from functools import wraps

def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        print(f"Arguments: args={args}, kwargs={kwargs}")
        
        result = func(*args, **kwargs)
        
        print(f"Returned: {result}")
        return result
    
    return wrapper

@log_call
def add(a, b):
    """Adds two numbers"""
    return a + b

add(5, 10)