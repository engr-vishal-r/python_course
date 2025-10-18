number=[10,3,-6,9,8,-1]
positive_numbers=[]

for num in number:
    if num < 0:
        continue
    positive_numbers.append(num)
print("Positive Numbers  : ", positive_numbers)