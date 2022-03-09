from flask import render_template
from homeconomy.server import server

@server.route('/')
def index():
    return render_template('index.html')
