import sys

if len(sys.argv) == 2:
    print("Error!!! Enter first name and last name")
    sys.exit()

first_name=sys.argv[1]
last_name=sys.argv[2]

#format the name
email=(first_name.lower().replace(" ",".")+last_name+"@vishal.com")
fulname="".join(first_name.lower().replace(" ",".")+last_name)

print("first name ", first_name)
print("last name ", last_name)
print("full name ", fulname)
print("Generate Email id  :", email)