#tuples are mentioned in () and is immutable, so you can’t modify, append, or remove elements.
#it maintains index order same like list

profile_info= ("vishal",9444771577,30,"male","Kaveripakkam")

print(profile_info[1])
print("count the element  --->", profile_info.count(30))

#must use comma, to concat tuple
profile_info1=("R",)

concat_tuple= profile_info + profile_info1
print(concat_tuple)