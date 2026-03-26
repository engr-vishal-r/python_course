import sys

if len(sys.argv) == 2:
    print("Error!!! Enter first name and last name")
    sys.exit()

name_provided=" ".join(sys.argv[1:])


#format the name
email="".join(name_provided.lower().replace(" ",".")+"@company.com")

print("first name ", name_provided)
print("Generate Email id  :", email)