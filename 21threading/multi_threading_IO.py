import threading
import time

def download():
    print("Start downloading...")
    time.sleep(5)
    print("Download complete!")

t1 = threading.Thread(target=download)
t2 = threading.Thread(target=download)

t1.start()
t1.join()
t2.start()
t2.join()