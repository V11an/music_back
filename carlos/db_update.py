import sqlite3

db = 'music_mentor.db'

connie = sqlite3.connect('db')
cursor = connie.cursor()

# update_query = 

# cursor.execute("UPDATE student SET surname = 'kipchoge'")
cursor.execute("UPDATE student SET surname = 'changed' WHERE firstname= 'Eliud' ")

# db.execute('UPDATE users SET name = ?, age = ? WHERE id = ?', [name, age, user_id])

connie.commit()
connie.close()