from flask import Flask

server = Flask(__name__)
server.env = 'development'

@server.route('/')
def home():
    return '<h1>Homeconomy!</h1>'

if __name__ == '__main__':
    server.run('0.0.0.0', port=80, debug=True)
