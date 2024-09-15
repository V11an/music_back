import sqlite3


db = 'music_mentor.db'

connie = sqlite3.connect('db')
cursor = connie.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS student(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               firstname TEXT,
               surname TEXT,
               email TEXT,
               password INTEGER
)
""")

connie.commit()
connie.close()

 