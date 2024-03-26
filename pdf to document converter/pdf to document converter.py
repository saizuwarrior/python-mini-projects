import pdf2docx

old_pdf = "new_pdf.pdf"
new_doc = "new.docx"

try:
    obj = pdf2docx.Converter(old_pdf)
    obj.convert(new_doc)
    obj.close()
    print("Conversion successful!")
except Exception as e:
    print("An error occurred during conversion:", e)