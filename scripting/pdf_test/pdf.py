import PyPDF2
import os
import sys

inputs = sys.argv[1:]

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()

    for pdf in pdf_list:
        my_file = os.path.join(THIS_FOLDER, pdf)
        merger.append(my_file)
    merger.write('merged.pdf')


pdf_combiner(inputs)
