import pikepdf
from pathlib import Path

input_pdf = Path(r"E:\Users\vishal\Downloads\EAadhaar_0000004577606120230830051926_18032026145550.pdf")
password = "VISH1995"

# Create output filename in the same folder
output_pdf = input_pdf.parent / f"{input_pdf.stem}_UL.pdf"

with pikepdf.open(input_pdf, password=password) as pdf:
    pdf.save(output_pdf)

print(f"Password removed successfully! Saved as: {output_pdf}")