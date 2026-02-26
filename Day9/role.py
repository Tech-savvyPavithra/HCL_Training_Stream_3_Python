from functools import wraps

# Simulated current user
class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role

# Global current user (like session user)
current_user = User("Pavi", "admin")

def requires_role(role):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if current_user.role != role:
                raise PermissionError(
                    f"Access denied! Required role: {role}"
                )
            return func(*args, **kwargs)
        return wrapper
    return decorator

@requires_role("admin")
def delete_user():
    return "User deleted successfully"

print(delete_user())