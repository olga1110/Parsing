from sqlalchemy import Column, Integer, Unicode, String, UniqueConstraint, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base


CBase = declarative_base()

class CPerson(CBase):

    __tablename__ = 'person'

    id = Column(Integer, primary_key = True)
    lastname = Column(Unicode, nullable=False)
    firstname = Column(Unicode, nullable=False)
    secondname = Column(Unicode)
    age = Column(Integer(), nullable=False)
    snils = Column(Unicode)
    birthdate = Column(Unicode, nullable=False)
    phone = Column(Unicode)

    snils_unique = UniqueConstraint('snils')

    def __repr__(self):
        return 'CPerson<id = %d, lastname = %s, firstname = %s, secondname = %s, age = %d, snils = %s, birthdate = %s, phone = %s>' % (self.id, self.lastname, self.firstname,\
                                                                                                                                           self.secondname, self.age, self.snils, self.birthdate, self.phone)

class CAddress(CBase):

    __tablename__ = 'address'
    id = Column(Integer(), primary_key=True)
    person_id = Column(Integer(), ForeignKey('person.id'))
    zipcode = Column(Unicode())
    country = Column(Unicode(), nullable=False)
    region = Column(Unicode(), nullable=False)
    type_place = Column(Unicode(), nullable=False)
    place_name = Column(Unicode(), nullable=False)
    street_name = Column(Unicode())
    house = Column(Integer(), nullable=False)
    apartment = Column(Integer())

    p_person_id = relationship('CPerson', foreign_keys=[person_id])

    def __repr__(self):
        return 'CAddress<id = %d, person_id = %d, zipcode = %s, country = %s, region = %s, type_place =  = %s, place_name = %s, street_name = %s, house = %d, apartment = %d>' % (
        self.id, self.person_id, self.zipcode, self.country, self.region, self.type_place, self.place_name, self.street_name, self.house, self.apartment)


if __name__ == '__main__':

    name_db = 'client.db'
    path_db = 'sqlite:///' + name_db
    engine = create_engine(path_db)
    session = sessionmaker(bind=engine)()


    # проверка записей в таблицах
    result = session.query(CAddress).all()
    for i in result:
        print(i)

    result = session.query(CPerson).all()
    for i in result:
        print(i)



