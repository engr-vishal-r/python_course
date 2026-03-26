num_list=[1,2,3,4,5,6,7,8]
n=3

result=[]

for i in range(0,len(num_list),n):
    result.append(num_list[i:i+n])

print(result)