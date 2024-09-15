import sqlite3


db = 'music_mentor.db'

connie = sqlite3.connect('db')
cursor = connie.cursor()

cursor.execute("""
               INSERT INTO student(firstname, surname, email, password)
               VALUES ('David', 'Rudisha', 'drudisha@gmail.com', 12345678),
                ('Eliud', 'Kipchoge', 'ekipchoge@gmail.com', 12345678)
""")

connie.commit()
connie.close()

 