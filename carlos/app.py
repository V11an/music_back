from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Variable name for Database
db = 'music_mentor.db'

@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        connie = sqlite3.connect('db')
        cursor = connie.cursor()

        email = request.form['email']
        password = request.form['password']
        # print(email, password)

        query_login = "SELECT email, password FROM student WHERE email='"+email+"' and password='"+password+"' "
        cursor.execute(query_login)

        results = cursor.fetchall()

        if len(results) == 0:
            print ("incorrect credentials")
        else:
            return render_template('home.html')

    # connie.close()
    return render_template('log.html')



@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else :
        student_details = (
            request.form['firstname'],
            request.form['surname'],
            request.form['email'],
            request.form['password'],
        )
        insert_student(student_details)
        # return redirect ('/student_list')
        return 'Student registered successfully'



def insert_student(student_details):
    connie = sqlite3.connect('db')
    sql_insert = 'INSERT INTO student (firstname, surname, email, password) VALUES (?, ?, ?, ?)'
    cursor = connie.cursor()
    cursor.execute(sql_insert, student_details)
    connie.commit()
    connie.close()
    


# To display list of students
@app.route('/student_list')
def student_list():
    student_data = query_student_list()
    return render_template('student_list.html', student_data = student_data)


# Function to connect to DB and fetch the list of students in table (student)
def query_student_list():
    connie = sqlite3.connect('db')
    cursor = connie.cursor()
    cursor.execute("""
SELECT * FROM student
""")
    student_data = cursor.fetchall()
    print(student_data[0][3])
    return student_data




# search function
# # ('/login', methods=['GET', 'POST'])
# @app.route('/search', methods =['GET', 'POST'])
# def search_list():
#     search_data = search_route()
#     return render_template('search_list.html', search_data = search_data)

@app.route('/search', methods =['GET', 'POST'])
def search_route():
    if request.method == 'POST':
        connie = sqlite3.connect('db')
        cursor = connie.cursor()

        name = request.form['name']
        # password = request.form['password']
        # print(email, password)

        # query_search = "SELECT * FROM student WHERE UPPER(firstname='"+name+"')  "
        # query_search = "SELECT * FROM student WHERE UPPER(firstname='"+name+"') or UPPER(surname='"+name+"') "
        query_search = f"SELECT * FROM student WHERE UPPER(firstname) LIKE '%{name}%' OR UPPER(surname) LIKE '%{name}%'"
        cursor.execute(query_search)

        search_data = cursor.fetchall()

        if len(search_data) == 0:
            print ("NO SUCH USER")
        else:
            return render_template('search_list.html', search_data = search_data)

    # connie.close()
    return render_template('search_page.html')



# def search_query():
#     connie = sqlite3.connect('db')
#     cursor = connie.cursor()
#     cursor.execute("""
# SELECT * FROM student WHERE UPPER(firstname) = 'eliud'
# """)
#     search_data = cursor.fetchall()
#     print(search_data)
#     return search_data





if __name__ == '__main__':
    app.run(debug=True)

