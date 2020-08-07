import PyPDF2
import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, "watermark.pdf")
my_file2 = os.path.join(THIS_FOLDER, "merged.pdf")

template = PyPDF2.PdfFileReader(open(my_file2, 'rb'))
watermark = PyPDF2.PdfFileReader(open(my_file, 'rb'))

output = PyPDF2.PdfFileWriter()

for item in range(template.getNumPages()):
    page = template.getPage(item)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open('watermaked.pdf', "wb") as file:
        output.write(file)
