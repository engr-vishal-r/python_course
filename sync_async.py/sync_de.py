import threading

counter = 0

lock = threading.Lock()

def safe_increment():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1


t1 = threading.Thread(target=safe_increment)
t2 = threading.Thread(target=safe_increment)

t1.start()
t2.start()
t1.join()
t2.join()

print("Counter:", counter)  # NOT always 200000
