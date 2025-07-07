import sys

if len(sys.argv) == 2:
    print("Error!!! Enter first name and last name")
    sys.exit()

first_name=sys.argv[1]
last_name=sys.argv[2]

#format the name
email="".join(first_name.lower().replace(" ",".")+last_name+"@vishal.com")

print("first name ", first_name)
print("last name ", last_name)
print("Generate Email id  :", email)
