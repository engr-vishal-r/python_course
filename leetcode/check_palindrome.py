def is_palindrome(number):
    if number > 0:
        original_num = number
        reverse = 0
        while number > 0:
            digit = number % 10
            reverse = reverse * 10 + digit
            number //= 10
        if original_num == reverse:
           return 'is palindrome'
        else:
            return 'not palindrome'
    else:
        return 'Number should be greater than 0'

if __name__ == "__main__":
    number = int(input("Enter Number to Check Palindrome: "))
    print(is_palindrome(number))
    