import pikepdf
import os

folder = "pdf_files"
password = "your_password"

for file in os.listdir(folder):
    if file.endswith(".pdf"):
        input_path = os.path.join(folder, file)
        output_path = os.path.join(folder, "unlocked_" + file)

        with pikepdf.open(input_path, password=password) as pdf:
            pdf.save(output_path)

        print(f"{file} unlocked")