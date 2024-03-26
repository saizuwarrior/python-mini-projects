from docx2pdf import convert

try:
    convert("new.docx", "new_pdf.pdf")
    print("Conversion successful.")
except Exception as e:
    print(f"An error occurred: {e}")