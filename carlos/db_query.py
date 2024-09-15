import sqlite3


db = 'music_mentor.db'

connie = sqlite3.connect('db')
cursor = connie.cursor()

cursor.execute("""
SELECT * FROM student
""")

student_info = cursor.fetchall()

for student in student_info:
    print(student)

connie.commit()
connie.close()
