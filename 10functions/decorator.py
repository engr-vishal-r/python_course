def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print("Before the function call")
        result = original_function(*args, **kwargs)
        print("After the function call")
        return result
    return wrapper_function

@decorator_function
def say_hello():
    print("Hello!")

say_hello()