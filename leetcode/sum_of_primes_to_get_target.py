number = 777
total = 0
prime_digits = {2, 3, 5, 7}  # using a set for O(1) lookup

while number > 0:
    digit = number % 10  # get last digit
    if digit in prime_digits:
        total += digit
    number //= 10  # remove last digit

print(total)