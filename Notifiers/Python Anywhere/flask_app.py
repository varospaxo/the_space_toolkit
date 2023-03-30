from flask import Flask,render_template, request
from flask_mysqldb import MySQL
import json

app = Flask(__name__, template_folder='template')

app.config['MYSQL_HOST'] = 'insolcity.mysql.pythonanywhere-services.com'
app.config['MYSQL_USER'] = 'insolcity'
app.config['MYSQL_PASSWORD'] = 'pythonproject'
app.config['MYSQL_DB'] = 'insolcity$default'

mysql = MySQL(app)

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return "use /form"

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        location = request.form['location']
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO users VALUES(%s,%s,%s)''',(email,password,location))
        mysql.connection.commit()
        cursor.close()
        return "Done!"

@app.route('/delete')
def delete():
    return render_template('delete.html')

@app.route('/delete_login', methods = ['POST', 'GET'])
def delete_login():
    if request.method == 'GET':
        return "use /delete"

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor()


        cursor.execute (''' DELETE FROM users WHERE email = (%s) AND password = (%s)''', (email,password))
        count = cursor.rowcount
        if count == 1:
            mysql.connection.commit()
            cursor.close()
            return "Email deleted!"
        elif count == 0:
            return "Email or Password is incorrect."
        else:
            return "Something went wrong. Please try again later."





@app.route('/api', methods = ['POST', 'GET'])
def handle_request():


    email = str(request.args.get('email'))
    password = str(request.args.get('password'))
    location = str(request.args.get('location'))

    data_set = {'email': email, 'location' : location}

    json_data = json.dumps(data_set)

    cursor = mysql.connection.cursor()
    cursor.execute(''' INSERT INTO users VALUES(%s,%s,%s)''',(email,password,location))
    mysql.connection.commit()
    cursor.close()

    return json_data




