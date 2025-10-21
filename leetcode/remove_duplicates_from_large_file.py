def remove_duplicates(input_file, output_file):
    seen = set()
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            if line not in seen:
                outfile.write(line)
            seen.add(line)
            
remove_duplicates('F:/python_tutorial/attendance.csv', 'F:/python_tutorial/output.csv')