import random

# Decorator definition
def retry_decorator(retries=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt + 1} failed: {e}")
            raise Exception("All retries failed")
        return wrapper
    return decorator

# Simulated unstable function
@retry_decorator(retries=3)
def flaky_function():
    if random.choice([True, False]):
        raise ValueError("Something went wrong!")
    return "Success!"

# Call the decorated function
print(flaky_function())
