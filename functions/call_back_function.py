#Callback Function passed into another function to be called later.

def greet(name):
    return f"Hello {name}"

def process(callback):
    print(callback("Vishal"))
process(greet)