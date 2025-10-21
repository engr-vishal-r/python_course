shared_counter = 0

def increment():
    global shared_counter
    for _ in range(100000):
        shared_counter += 1

def main():
    increment()
    increment()

main()
print("Final:", shared_counter)