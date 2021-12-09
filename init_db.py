import sqlite3

def create_db():
    connection = sqlite3.connect('db/database.db')

    with open('db/schema.sql') as f:
        connection.executescript(f.read())

    cur = connection.cursor()

    connection.commit()
    connection.close()