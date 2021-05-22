import sqlite3

conn = sqlite3.connect('database.db')
conn.execute(
    'CREATE TABLE weapons (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, stock INTEGER)'
)
conn.commit()
conn.close()
