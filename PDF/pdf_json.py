import json
import os

from pdf_page_read import pdf_page_read


def export_as_json(pdf_path, json_path):
    filename = os.path.splitext(os.path.basename(pdf_path))[0]
    data = {'Filename': filename}
    data['Pages'] = []

    counter = 1
    for page in pdf_page_read(pdf_path):
        text = page[0:100]
        page = {'Page_{}'.format(counter): text}
        data['Pages'].append(page)
        counter += 1

    with open(json_path, 'w', encoding='UTF-8') as fh:
        json.dump(data, fh)


if __name__ == '__main__':
    file_name = 'Services'
    pdf_path = file_name + '.pdf'
    json_path =  file_name + '.json'
    export_as_json(pdf_path, json_path)