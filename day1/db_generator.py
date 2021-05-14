import sqlite3

connect = sqlite3.connect('database.db')
connect.execute('CREATE TABLE MENUS(ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME TEXT, PRICE INTEGER)')
cursor = connect.cursor()
cursor.executemany(
    'INSERT INTO MENUS(NAME, PRICE) VALUES (?, ?)',
    [
        ('Espresso', 3000),
        ('Americano', 4100), 
        ('CafeLatte', 4600)
    ]
)
connect.commit()
connect.close()
