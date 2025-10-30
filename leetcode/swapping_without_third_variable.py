first_num=100
second_num=500

print('Before Swapping : ')

print(f'first number {first_num} ')
print(f'second number {second_num} ')


first_num=first_num^second_num
second_num=first_num^second_num
first_num=first_num^second_num

print('After Swapping : ')

print(f'first number {first_num} ')
print(f'second number {second_num} ')

# 🔹 Pythonic swap
first_num, second_num = second_num, first_num

print("\Pythonic Swapping:")
print(f"first number = {first_num}")
print(f"second number = {second_num}")