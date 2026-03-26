import multiprocessing

def square(x):
    return x * x

if __name__ == "__main__":
    with multiprocessing.Pool(4) as pool:
        results = pool.map(square, [1, 2, 3, 4])
        print(results)