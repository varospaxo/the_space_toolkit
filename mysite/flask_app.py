
# A very simple Flask Hello World app for you to get started with...

from flask import Flask,render_template
app = Flask(__name__, template_folder='')

@app.route('/')
def form():
    return render_template('index.html')
@app.route('/index.html')
def index():
    return render_template('index.html')
@app.route('/email-notif.html')
def sub():
    return render_template('email-notif.html')
@app.route('/email-notif1.html')
def sub1():
    return render_template('email-notif1.html')