from PyPDF2 import PdfMerger

pdfs = [
    "C:/Users/vishal/OneDrive/capgemini/vishalr_education_documents/ug_degree_documents/vishalr_marksheet.pdf",
    "C:/Users/vishal/OneDrive/capgemini/vishalr_education_documents/ug_degree_documents/vishalr_ug_degree.pdf"
]

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("C:/Users/vishal/OneDrive/capgemini/vishalr_education_documents/ug_degree_documents.pdf")
merger.close()

print("PDFs merged successfully!")