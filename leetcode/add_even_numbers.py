num=5684
total=0

if num > 0:
    while num > 0:
        digit = num % 10
        if digit % 2 == 0:
            total += digit
        num//=10
    while total >= 10:
        total = sum(int(d) for d in str(total))
    print(total)
else:
    print('Number must be greater than 0')