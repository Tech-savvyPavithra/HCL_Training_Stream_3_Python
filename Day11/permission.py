# Dummy current user object
class User:
    def __init__(self, role):
        self.role = role

# Example current user
current_user = User("test")   # Change role to admin

# Decorator function
def requires_role(role):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if current_user.role != role:
                raise PermissionError("You do not have permission to access this function.")
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Example usage
@requires_role("admin")
def delete_user():
    print("User deleted successfully!")

# Call the function
delete_user()