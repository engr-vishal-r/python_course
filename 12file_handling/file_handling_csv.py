content = input("Enter data (e.g., 1, John Doe, Present): ")

file_path = "attendance.csv"

try:
    with open(file_path, "r") as file:
        has_header = file.readline().strip() != ""
except FileNotFoundError:
    has_header = False

# Now write to the file
with open(file_path, "a") as file:
    if not has_header:
        file.write("S.no,StudentName,Present/Absent\n")
        print("Header added.")
    file.write(content + "\n")
    print("Data written successfully.")
