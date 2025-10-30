input = [77, 888, 991, 771, 777, 337]

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_digits = [num for num in input if is_prime(num)]

print(prime_digits)