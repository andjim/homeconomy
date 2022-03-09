from flask import Flask
from flask_sqlalchemy import SQLAlchemy

server = Flask(__name__)

server.env = 'development'
server.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./test.db'

db = SQLAlchemy(server)