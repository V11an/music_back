import sqlite3

db = 'music_mentor.db'

connie = sqlite3.connect('db')
cursor = connie.cursor()

# update_query = 

cursor.execute("DELETE FROM student WHERE firstname ='doe'")

connie.commit()
connie.close()