from flask import Flask,render_template, request
from flask_mysqldb import MySQL
import json

app = Flask(__name__, template_folder='')

app.config['MYSQL_HOST'] = ''
app.config['MYSQL_USER'] = ''
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = ''

mysql = MySQL(app)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return """<html><body><a href="https://launchmail.pythonanywhere.com/">Subscribe another email</a></br><a href="http://launchmail.pythonanywhere.com/delete">Unsubscribe</a></body></html>"""


    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # location = request.form['location']
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO users VALUES(%s,%s);''',(email,password))
        mysql.connection.commit()
        cursor.close()
        return """<html><body><p>Subscribed!</p></br><a href="https://launchmail.pythonanywhere.com/">Subscribe another email</a></br><a href="https://launchmail.pythonanywhere.com/delete">Unsubscribe</a></body></html>"""

@app.route('/delete')
def delete():
    return render_template('delete.html')

@app.route('/delete_login', methods = ['POST', 'GET'])
def delete_login():
    if request.method == 'GET':
        return """<html><body><a href="https://launchmail.pythonanywhere.com/">Resubscribe</a></body></html>"""

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor()


        cursor.execute (''' DELETE FROM users WHERE email = (%s) AND password = (%s)''', (email,password))
        count = cursor.rowcount
        if count >= 1:
            mysql.connection.commit()
            cursor.close()
            return """<html><body><a href="https://launchmail.pythonanywhere.com/">Resubscribe</a></body></html>"""
        elif count == 0:
            return "Email or Password is incorrect. For support contact crudespace@gmail.com."
        else:
            return "Something went wrong. Please try again later. For support contact crudespace@gmail.com."





@app.route('/api', methods = ['POST', 'GET'])
def handle_request():


    email = str(request.args.get('email'))
    password = str(request.args.get('password'))

    data_set = {'email': email, 'password': password}
    json_data = json.dumps(data_set)

    cursor = mysql.connection.cursor()
    cursor.execute(''' INSERT INTO users VALUES(%s,%s);''',(email,password))
    mysql.connection.commit()
    cursor.close()

    return json_data

@app.route('/reload', methods = ['POST', 'GET'])
def reload():
    return render_template('script.html')

