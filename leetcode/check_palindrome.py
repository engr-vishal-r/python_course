number=0
original_num=number
reverse=0

if number >0:
    while number > 0:
        digit =number % 10
        reverse = reverse * 10 + digit
        number = number // 10
    if original_num==reverse:
        print('is palindrome') 
    else:
        print('not palindrome')
else:
    print('Number should be greater than 0')