import random

# Decorator
def require_login(func):
    def wrapper(user, *args, **kwargs):
        if user.get("authenticated"):
            return func(user, *args, **kwargs)
        else:
            raise PermissionError("User not authenticated")
    return wrapper

# Function that requires authentication
@require_login
def view_dashboard(user):
    return f"Welcome, {user['name']}! You are logged in."

# Simulate users
authenticated_user = {"name": "Alice", "authenticated": True}
unauthenticated_user = {"name": "Bob", "authenticated": False}

# Randomly inject user
for _ in range(1):
    user = random.choice([authenticated_user, unauthenticated_user])
    try:
        print(view_dashboard(user))
    except Exception as e:
        print("Error:", e)