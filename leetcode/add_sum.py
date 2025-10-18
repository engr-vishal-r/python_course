def sum_till_last_digit(num):
    while num >= 9:  
        total = 0
        while num > 0:
            total += num % 10
            num //= 10
        num = total
    return num

number = 2885
result = sum_till_last_digit(number)
print(f"Final digit sum: {result}")