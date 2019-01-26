import psycopg2


with psycopg2.connect(host='127.0.0.1', user='postgres', password='postgres', dbname='postgres') as conn:
    with conn.cursor() as cursor:
        cursor.execute('drop table if exists product_items')
        cursor.execute('drop table if exists products')
        cursor.execute('drop table if exists categories')

        # try:
        cursor.execute("""

            create table

                categories
                (
                    id serial,                        
                    name character varying(60) NOT NULL UNIQUE,
                    descr text,
                    active boolean DEFAULT true NOT NULL,
                    CONSTRAINT categories_PK PRIMARY KEY (id)

                )
            """)
        # except psycopg2.ProgrammingError as e:
        #     print('Table already exists')
        # else:
        #     print('Table is created')

        cursor.execute("""

            create table

                products
                (
                    id serial,
                    name character varying(300) NOT NULL,                            
                    descr text,
                    price float(2) NOT NULL,
                    active boolean DEFAULT true NOT NULL,
                    categories_id integer,
                    CONSTRAINT products_PK PRIMARY KEY (id),
                    CONSTRAINT fk_categories foreign key (categories_id)
                    REFERENCES categories (id)

                )
            """)

        cursor.execute("""

            create table

                product_items
                (
                    id serial,
                    name character varying(300) NOT NULL,                         
                    price float(2) NOT NULL,
                    amount integer,
                    active boolean DEFAULT true NOT NULL,
                    products_id integer,
                    CONSTRAINT product_items_PK PRIMARY KEY (id),
                    CONSTRAINT fk_products foreign key (products_id)
                    REFERENCES products (id)

                )
            """)











