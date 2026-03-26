from multiprocessing import Process

def compute():
    for _ in range(10**7):
        pass

p1 = Process(target=compute)
p2 = Process(target=compute)

p1.start()
p2.start()