import pikepdf

old_pdf = pikepdf.Pdf.open("periodic classification.pdf")

no_entry = pikepdf.Permissions(extract=False)

old_pdf.save("protected pdf",encryption = pikepdf.Encryption(user="hello world",owner="uttkarsh",allow=no_entry))