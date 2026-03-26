first_str='10'
second_str='20'

print("Before typecasting")
print(type(first_str))   #type checking
print(first_str+second_str)

first_num=int(first_str)
second_num=int(second_str)
print(type(first_num))
print("After typecasting")
print(first_num+second_num)