# miner_text_generator.py

import io

from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage


def pdf_page_read(pdf_path):
    with open(pdf_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh,
                                      caching=True,
                                      check_extractable=True):
            resource_manager = PDFResourceManager()
            file_handle = io.StringIO()
            converter = TextConverter(resource_manager, file_handle)
            page_interpreter = PDFPageInterpreter(resource_manager, converter)
            page_interpreter.process_page(page)

            text = file_handle.getvalue()
            yield text

            # close open handles
            converter.close()
            file_handle.close()


def extract_text(pdf_path):
    for page in pdf_page_read(pdf_path):
        print(page)
        print()


if __name__ == '__main__':
    print(extract_text('Services.pdf'))