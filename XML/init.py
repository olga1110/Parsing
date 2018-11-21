import sqlite3
from sqlalchemy import Column, Integer, Unicode, String, UniqueConstraint, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base


conn = sqlite3.connect("client.db")
cursor = conn.cursor()

cursor.execute('drop table if exists address')
cursor.execute('drop table if exists person')

cursor.execute("""
    create table
        person
        (
            id integer primary key autoincrement,
            lastname text not null,
            firstname text not null,
            secondname text,
            age integer not null,
            snils text,
            birthdate text,
            phone text,
            CONSTRAINT snils_unique UNIQUE (snils)
        )
    """)

cursor.execute("""
    create table
        address
        (
            id integer primary key autoincrement,
            person_id integer references person (id),
            zipcode text,
            country text not null,
            region text not null,
            type_place not null,        
            place_name text not null,
            street_name text,
            house integer not null,
            apartment integer           
                        
        )
    """)


if __name__ == '__main__':
    conn.commit()



