n=int(input("Enter number to find all prime numbers up to  : "))

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = [i for i in range(2, n+1) if is_prime(i)]
print(primes)