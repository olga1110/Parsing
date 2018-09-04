# -*- coding: utf-8 -*-
from lxml import etree, objectify
from sqlalchemy import Column, Integer, Unicode, UniqueConstraint, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker, relationship
from DB_classes import *




name_db = 'client.db'
path_db = 'sqlite:///' + name_db
engine = create_engine(path_db)
session = sessionmaker(bind=engine)()





# def parseXML(xmlFile, session):
#     """Parse the XML file"""
with open('document1.xml', encoding = 'utf-8') as f:
    xml = f.read()

root = objectify.fromstring(xml)

#Обработка файла
# person
last_name = root.Person.FIO.LastName
first_name = root.Person.FIO.FirstName
# print('first_name', first_name)
second_name = root.Person.FIO.SecondName
# print('second_name', second_name)
age = root.Person.Age.Years
# print('age', age)
snils = root.Person.SNILS
# print('snils', snils)
birthdate = root.Person.BirthDate
# print('birthdate', birthdate)
phone = root.Person.Phones.Phone
# print('phone', phone)

# address

cursor.execute("""
    create table
        address
        (
            id integer primary key autoincrement,
            person_id integer references person (id),
            zipcode text,
            address_type text not null,
            district_name text,
            city_name text,
            street_name text,
            house text not null,
            apartment text           

        )
    """)
zipcode = root.Person.Fields.ZipCode
country = root.Person.Fields.Country
region = root.Person.Fields.TerritorySubjectName
type_place = root.Person.Fields.PlaceTypeName
place_name = root.Person.Fields.Place
street_name = root.Person.Fields.Street
house = root.Person.Fields.House
apartment = root.Person.Fields.Appartment
#///////////////////////////////////////////////////
print('zipcode', zipcode)
print('country', country)
print('region', region)
print('type_place', type_place)
print('place_name', place_name)
print('street_name', street_name)
print('house', house)
print('apartment', apartment)
#///////////////////////////////////////////////////
#вставка в БД

session.add(CPerson(lastname=str(last_name), firstname=str(first_name), secondname=str(second_name), age=int(age), snils=str(snils), birthdate=str(birthdate), phone=str(phone)))
session.commit()
    # в цикле выводим всю информацию про элементы (тэги и текст).
    # for appt in root.getchildren():
    #     for e in appt.getchildren():
    #         print("%s => %s" % (e.tag, e.text))
    #     print()
    #
    # # пример как менять текст внутри элемента.
    # root.appointment.begin = "something else"
    # print(root.appointment.begin)
    #
    # # добавление нового элемента.
    # root.appointment.new_element = "new data"
    #
    # # удаляем аннотации.
    # objectify.deannotate(root)
    # etree.cleanup_namespaces(root)
    # obj_xml = etree.tostring(root, pretty_print=True)
    # print(obj_xml)
    #
    # # сохраняем данные в файл.
    # with open("new.xml", "w") as f:
    #     f.write(obj_xml)


# if __name__ == "__main__":
#     # f = r'path\to\sample.xml'
#     parseXML('document1.xml', session)