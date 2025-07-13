correct_pin = 1234
entered_pin = None 

while entered_pin != correct_pin:
    try:
        entered_pin = int(input('Enter your correct pin here: '))
    except ValueError:
        print("Please enter numbers only.")
print('Access Granted')