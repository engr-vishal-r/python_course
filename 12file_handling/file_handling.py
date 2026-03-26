content = input("Enter new entry ")


with open("docs.txt", "a+") as file:
    file.seek(0)  # Move to the beginning of the file
    first_line = file.readline()

    if not first_line:  # If file is empty
        file.write("StudentNo,Name,Grade\n")  # Write header

    file.write(content + "\n")  # Append new entry

    # Rewind again to print the full content
    file.seek(0)
    print("\n--- File Content ---\n")
    for line in file:
        column=(line.split(","))
        print(column[1])