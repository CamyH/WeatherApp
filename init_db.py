import sqlite3

connection = sqlite3.connect('db/database.db')


with open('db/schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

#cur.execute("INSERT INTO data (title) VALUES (?)",
#            ('Edinburgh',))

connection.commit()
connection.close()