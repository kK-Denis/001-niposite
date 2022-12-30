
from datetime import datetime
from flask import render_template

from Flaskapp import app

@app.route('/')
@app.route('/home')
def home():
    now = datetime.now()
    formatted_now = now.strftime("%A, %d, %B, %Y at %X")

    return render_template(
        "index.html",
        title = "nipo.ke",
        message = "Nipo, Site!",
        content = " on " + formatted_now)

@app.route('/about')
def about():
    return render_template(
        "about.html",
        title = "kuhusu site",
        content = "Example app page for Flask.")

@app.route('/api/data')
def get_data():
    return app.send_static_file('data.json')