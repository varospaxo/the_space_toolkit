
# A very simple Flask Hello World app for you to get started with...

from flask import Flask,render_template
app = Flask(__name__, template_folder='')

@app.route('/')
def form():
    return render_template('index.html')