import os
import xml.etree.ElementTree as xml
from xml.dom import minidom
from pdf_page_read import pdf_page_read


def export_as_xml(pdf_path, xml_path):
    filename = os.path.splitext(os.path.basename(pdf_path))[0]
    root = xml.Element('{filename}'.format(filename=filename))
    pages = xml.Element('Pages')
    root.append(pages)

    counter = 1
    for page in pdf_page_read(pdf_path):
        text = xml.SubElement(pages, 'Page_{}'.format(counter))
        text.text = page[0:100]
        counter += 1

    tree = xml.ElementTree(root)
    xml_string = xml.tostring(root, 'utf-8')
    parsed_string = minidom.parseString(xml_string)
    pretty_string = parsed_string.toprettyxml(indent='  ')

    with open(xml_path, 'w') as fh:
        fh.write(pretty_string)
    tree.write(xml_path)


if __name__ == '__main__':
    pdf_path = 'Services.pdf'
    xml_path = 'Services.xml'
    export_as_xml(pdf_path, xml_path)