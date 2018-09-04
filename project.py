# -*- coding: utf-8 -*-
import os
from lxml import etree, objectify
from sqlalchemy import Column, Integer, Unicode, UniqueConstraint, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker, relationship
from DB_classes import *

name_db = 'client.db'
path_db = 'sqlite:///' + name_db
engine = create_engine(path_db)
session = sessionmaker(bind=engine)()

path = os.getcwd()

def parseXML(file_name):
    with open(file_name, encoding='utf-8') as f:
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

    zipcode = root.Person.LivingAddress.Fields.ZipCode
    country = root.Person.LivingAddress.Fields.Country
    region = root.Person.LivingAddress.Fields.TerritorySubjectName
    type_place = root.Person.LivingAddress.Fields.PlaceTypeName
    place_name,_ = str(root.Person.LivingAddress.Fields.Place).split()
    street_name,_ = str(root.Person.LivingAddress.Fields.Street).split()
    house = root.Person.LivingAddress.Fields.House
    apartment = root.Person.LivingAddress.Fields.Appartment
    #///////////////////////////////////////////////////
    # print('zipcode', zipcode)
    # print('country', country)
    # print('region', region)
    # print('type_place', type_place)
    # print('place_name', place_name)
    # print('street_name', street_name)
    # print('house', house)
    # print('apartment', apartment)
    #///////////////////////////////////////////////////
    #вставка в БД

    session.add(CPerson(lastname=str(last_name), firstname=str(first_name), secondname=str(second_name), age=int(age), snils=str(snils), birthdate=str(birthdate), phone=str(phone)))
    session.commit()
    person_id = session.query(CPerson.id).order_by(CPerson.id.desc()).first()
    session.add(CAddress(person_id = person_id[0], zipcode=str(zipcode), country=str(country), region=str(region), type_place=str(type_place), place_name=str(place_name), street_name=str(street_name), house=int(house), apartment=int(apartment)))
    session.commit()



if __name__ == "__main__":
    parseXML(os.path.join(path, 'input_documents','11111222222211.xml'))