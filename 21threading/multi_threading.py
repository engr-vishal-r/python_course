import threading
import time

def worker(n):
    print(f"Thread-{n} started")
    time.sleep(3)
    print(f"Thread-{n} finished")

threads = []

for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join() #synchronous behaviour

print("All threads finished.")