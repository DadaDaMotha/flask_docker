import flask

server = flask.Flask(__name__)

@server.route('/')
def hello():
    return 'Hello, World!'