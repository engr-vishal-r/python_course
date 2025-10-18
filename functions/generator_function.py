# Generator Function Uses yield to return one value at a time.

def countdown(n):
    while n > 0:
        yield n
        n -= 1

new_func=countdown(5)

for value in new_func:
    print(value)