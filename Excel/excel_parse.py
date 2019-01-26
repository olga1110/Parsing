import xlrd
import xlwt
import copy
from pprint import pprint
from log_config import log_parse_init

log = log_parse_init()
book_list = []

rb = xlrd.open_workbook('АИС.xls', formatting_info=True)
sheet = rb.sheet_by_index(0)
for rownum in range(sheet.nrows):
    row = sheet.row_values(rownum)
    row_list = []
    book_list.append(row_list)
    for c_el in row:
        if isinstance(c_el, float):
            row_list.append(int(c_el))
        else:
            row_list.append(c_el)

# pprint(book_list)
# print(len(book_list))

#Выполняем проверки
# Первая строка содержит заголовок
for index, row in enumerate(copy.deepcopy(book_list[1:])):
    if not isinstance(row[2], int):
        log.error('Строка %s, Колонка=3: регистрационный номер участника должен быть в целочисленном формате' % (index+1))
        del book_list[index+1]
    # # day, month, year = row[3].split('.')
    # # if year < 1995:
    # #     print('Строка {}, Дата постановки на учет раньше 1995 года'.format(row + 1))
    # if len(str(row[18])) != 4:
    #     print('Строка {}, Cерия документа должна содержать 4 символа'.format(index + 1))
    # if len(str(row[19])) != 6:
    #     print('Строка {}, Номер документа должен содержать 6 символов'.format(index + 1))

# Записываем в новый файл корректные строки

from datetime import datetime

font0 = xlwt.Font()
font0.name = 'Times New Roman'
font0.colour_index = 2
font0.bold = True

style0 = xlwt.XFStyle()
style0.font = font0

# style1 = xlwt.XFStyle()
# style1.num_format_str = 'DD-MM-YYYY'

wb = xlwt.Workbook()
ws = wb.add_sheet('Отчет_исправленный')

ws.write(0, 0, 'После проверки', style0)

for row_number, row in enumerate(book_list):
    for col_number, cell in enumerate(row):
        ws.write(row_number+1, col_number+1, cell)

wb.save('АИС_испр.xls')

