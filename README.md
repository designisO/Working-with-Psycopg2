# Python & Postgres

For today I wanted to review how to connect to postgres using python. The goal was to learn more about the connector library called "Pyscopg2". It is used as an adapter to connect to the postgres database. This is a great tool to use as an alternate to SQLAlchemy as well. 

The cursor is used to create and read data from the database using SQL statements. You can fetch the data using the fetchone() or fetchall() methods. You have the option to use executemany() for querying all data in a sequence. 

Dictionary-like cursor allows the access to attributes similar to python dictionaires instead of the tuples displayed. 


### Installation

pip install psycopg2


