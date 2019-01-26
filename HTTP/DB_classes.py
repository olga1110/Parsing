#!/usr/bin/env python3

from sqlalchemy import Column, Integer, Unicode, String, Boolean, Float, UniqueConstraint, ForeignKey, create_engine, select
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from pprint import pprint

CBase = declarative_base()

class CCategory(CBase):

    __tablename__ = 'categories'

    id = Column(Integer(), primary_key = True)
    name = Column(String(60), nullable=False)
    descr = Column(Unicode())
    active = Column(Boolean, default=True)

    check_1 = UniqueConstraint('name')

    def __init__(self, name, descr, active=True):
        self.name = name
        self.descr = descr
        self.active = active

    def __repr__(self):
        return 'CCategory<id = %d, name = %s, descr = %s>' % (self.id, self.name, self.descr)


class CProduct(CBase):

    __tablename__ = 'products'

    id = Column(Integer(), primary_key = True)
    name = Column(String(300), nullable=False)
    descr = Column(Unicode())
    price = Column(Float(9,2), nullable=False)
    categories_id = Column(Integer(), ForeignKey('categories.id'))
    active = Column(Boolean, default=True)


    def __init__(self, name, descr, price, categories_id, active=True):
        self.name = name
        self.descr = descr
        self.price = price
        self.categories_id = categories_id
        self.active = active

    def __repr__(self):
        return 'CProduct<id = %d, name = %s, descr = %s, price = %d>' % (self.id, self.name, self.descr, self.price)


class CProductItems(CBase):

    __tablename__ = 'product_items'

    id = Column(Integer(), primary_key=True)
    name = Column(String(300), nullable=False)
    price = Column(Float(9,2), nullable=False)
    amount = Column(Integer())
    products_id = Column(Integer(), ForeignKey('products.id'))
    active = Column(Boolean, default=True)


    def __init__(self, name, price, amount, products_id, active=True):
        self.name = name
        self.price = price
        self.amount = amount
        self.products_id = products_id
        self.active = active

    def __repr__(self):
        return 'CProductItems<id = %d, name = %s, price = %d, amount = %d>' % (self.id, self.name, self.price, self.amount)


if __name__ == '__main__':
    engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/postgres')
    session = sessionmaker(bind=engine)()

    sets = CCategory('sets', 'Готовые кухонные гарнитуры')
    session.add(sets)
    session.commit()


    # result = engine.execute("select* from categories")
    # # result = engine.execute("select* from products where id =(select max(id) from products)")
    # print(result.fetchall())
    # # obj = session.query(CProduct.id).order_by(CProduct.id.desc()).first()[0]
    # # print(obj)
    # # pprint(session.query(CProduct).all())
    # # pprint(session.query(CProductItems).all())

    # pprint(engine.execute("select* from products").fetchall())
    # pprint(engine.execute("select* from product_items").fetchall())




