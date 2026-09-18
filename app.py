from flask import Flask, render_template, request
from db_config import db, cursor
import random

app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    return render_template('index.html')


# Student Registration Page
@app.route('/registerpage')
def registerpage():
    return render_template('register.html')


# Student Login Page
@app.route('/loginpage')
def loginpage():
    return render_template('login.html')


# Admin Login Page
@app.route('/adminloginpage')
def adminloginpage():
    return render_template('admin_login.html')


# Dashboard
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


# Register Student
@app.route('/register', methods=['POST'])
def register():

    username = "STD" + str(random.randint(1000,9999))
    password = "COL" + str(random.randint(10000,99999))

    sql = """
    INSERT INTO students
    (
    username,
    password,
    name,
    email,
    phone,
    age,
    gender,
    address,
    academic_year,
    tenth_marks,
    twelfth_marks,
    merit_rank,
    allotment_letter,
    course,
    status
    )
    VALUES
    (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    values = (
        username,
        password,
        request.form['name'],
        request.form['email'],
        request.form['phone'],
        request.form['age'],
        request.form['gender'],
        request.form['address'],
        request.form['academic_year'],
        request.form['tenth_marks'],
        request.form['twelfth_marks'],
        request.form['merit_rank'],
        request.form['allotment_letter'],
        request.form['course'],
        request.form['status']
    )

    cursor.execute(sql, values)
    db.commit()

    return render_template(
        'success.html',
        username=username,
        password=password
    )


# Student Login
@app.route('/login', methods=['POST'])
def login():

    username = request.form['username']
    password = request.form['password']

    sql = """
    SELECT * FROM students
    WHERE username=%s AND password=%s
    """

    cursor.execute(sql, (username, password))

    student = cursor.fetchone()

    if student:

        return render_template(
            'student_profile.html',
            student=student
        )

    return "Invalid Username or Password"


# Admin Login
@app.route('/adminlogin', methods=['POST'])
def adminlogin():

    email = request.form['email']
    password = request.form['password']

    if email == "admin@college.com" and password == "admin123":

        return render_template('dashboard.html')

    return "Invalid Admin Email or Password"


# View All Students
@app.route('/students')
def students():

    cursor.execute("SELECT * FROM students")

    data = cursor.fetchall()

    return render_template(
        'students.html',
        students=data
    )


if __name__ == '__main__':
    app.run(debug=True)