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

# instruments page
@app.route('/instrumentPage')
def instrument_list():
    return render_template('instruments.html')

# list of mentors for a specific instrument
@app.route('tutor_instrument')
def tutor_instrument():
    tutor_data = query_tutor_list()
    return render_template('tutor_list.html', tutor_data = tutor_data)

# Function to connect to DB and fetch the list of tutors for a specific instrument in table (tutor)
def query_tutor_list():
    connie = sqlite3.connect('db')
    cursor = connie.cursor()
    cursor.execute("""
SELECT * FROM tutor WHERE instrument='piano'
""")
    tutor_data = cursor.fetchall()
    print(tutor_data[0][3])
    return tutor_data


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


@app.route('/book/<int:tutor_id>')
def book_tutor(tutor_id):
    # Get student and tutor information
    student_id = get_current_student_id()
    tutor_info = get_tutor_info(tutor_id)

    # Create a booking request
    create_booking_request(student_id, tutor_id)

    return render_template('booking_success.html')

def create_booking_request(student_id, tutor_id):
    conn = sqlite3.connect(music_mentor.db)
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO bookings (student_id, tutor_id)
        VALUES (?, ?)
    ''', (student_id, tutor_id))

    conn.commit()
    conn.close()




if __name__ == '__main__':
    app.run(debug=True)

