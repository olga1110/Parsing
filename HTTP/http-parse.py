import requests
from bs4 import BeautifulSoup
from pprint import pprint

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship

from DB_classes import *

engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/postgres')
session = sessionmaker(bind=engine)()

BASE_URL = 'https://hoff.ru/catalog/kuhnya/kuhonnye_garnitury/gotovie_reshenia/modulnie/barselona/'

r = requests.get(BASE_URL)
soap = BeautifulSoup(r.text, 'html.parser')

prices = []
short_desc = []
full_desc = []
detail_href = []

for price in soap.find_all(class_='price-current'):
    prices.append(round(float(price.contents[0].replace(' ', '')), 2))

for desc in soap.select('div.elem-product__links > a'):
    short_desc.append(desc.contents[0].strip())
    detail_href.append('https://hoff.ru' + desc.get('href'))


# Переходим на страницу товара (product_detail)

for index, link in enumerate(detail_href):
    r = requests.get(link)
    soap = BeautifulSoup(r.text, 'html.parser')
    descr = soap.select('div.list-dotted')[0].get_text()
    full_desc.append(descr)
    session.add(CProduct(short_desc[index], descr, prices[index], 1))
    session.commit()
    product_id = session.query(CProduct.id).order_by(CProduct.id.desc()).first()[0]
    print(product_id)
    # Подгружаем данные по комплектующим товара
    item_names = []
    item_prices = []
    item_amounts = []
    for price in soap.select('div.list-complect')[0].find_all(class_='price'):
        item_prices.append(round(float(price.contents[0].replace(' ', '')), 2))

    for amount in soap.select('div.list-complect')[0].find_all(class_='amount'):
        item_amounts.append(amount.contents[0].replace(' шт.', ''))

    for name in soap.select('div.list-complect')[0].find_all('a'):
        item_names.append(name.get('title'))

    product_items = zip(item_names, item_prices, item_amounts)
    for index, item in enumerate(product_items):
        session.add(CProductItems(item_names[index], item_prices[index], item_amounts[index], product_id))
        session.commit()

# Запись подробного описания в файл
# with open('full_desc.txt', 'w', encoding='utf-8') as f:
#     for line in full_desc:
#         f.write(line)

# products_list = list(zip(short_desc, full_desc, prices))
# for product in products_list:
#     session.add(CProduct(product[0], product[1], product[2], 1))
#     session.commit()
#






