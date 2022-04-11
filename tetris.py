from flask import Flask
tetris = Flask(__name__)
@tetris.route('/')
def hello_world():
    return 'word!'