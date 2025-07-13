correct_pin = 1234
entered_pin = None 
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    try:
        entered_pin = int(input('Enter your correct pin here: '))
        if entered_pin == correct_pin:
            print('Access Granted')
            break
        else:
            print('Incorrect PIN')
            attempts += 1
    except ValueError:
        print("Numbers only please.")
        attempts += 1
else:
    print('Access Denied: Too many attempts')
