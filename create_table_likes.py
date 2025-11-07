import sqlite3

connection = sqlite3.connect('sqlite.db', check_same_thread=False)
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE like (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        post_id TEXT UNIQUE NOT NULL,
        user_id TEXT NOT NULL );
    ''')

connection.commit()
connection.close()