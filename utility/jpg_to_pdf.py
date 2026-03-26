from PIL import Image
from pathlib import Path

input_image = Path(r"C:\Users\vishal\OneDrive\Reps_docs\vishal_r_REPS_Relieving_Letter.jpeg")
output_pdf = input_image.parent / f"{input_image.stem}.pdf"

image = Image.open(input_image)

# Convert to RGB (important for JPG)
image = image.convert("RGB")

image.save(output_pdf)

print(f"JPG converted to PDF successfully! Saved as: {output_pdf}")