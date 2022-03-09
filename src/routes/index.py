from flask import render_template
from src.server import server

@server.route('/')
def index():
    return render_template('index.html')
