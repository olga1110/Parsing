import io
from pprint import pprint

from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage


def extract_text_from_pdf(pdf_path):
    resource_manager = PDFResourceManager()
    file_handle = io.StringIO()
    converter = TextConverter(resource_manager, file_handle)
    page_interpreter = PDFPageInterpreter(resource_manager, converter)

    with open(pdf_path, 'rb') as f:
        for page in PDFPage.get_pages(f,
                                      caching=True,
                                      check_extractable=True):
            page_interpreter.process_page(page)

        text = file_handle.getvalue()

   
    converter.close()
    file_handle.close()

    if text:
        return text


if __name__ == '__main__':
    pprint(extract_text_from_pdf('Services.pdf'))