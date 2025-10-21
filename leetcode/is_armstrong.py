def is_armstrong():
    number = int(input("Enter a number: ")) 
    power = len(str(number)) 
    sum = 0 
    temp = number 
    if number > 0:
        while temp > 0: 
            digit = temp % 10
            sum += digit ** power
            temp //= 10
        if number == sum:
            print(number, "is an Armstrong number")
        else: 
            print(number, "is not an Armstrong number")
    else:
        print(number, "Number must be greater than 0")

is_armstrong()