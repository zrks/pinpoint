import os
from flask import Flask, request


APP_KEY = os.environ['APP_KEY']
APP_SECRET = os.environ['APP_SECRET']
APP_SECRET_KEY = os.environ['APP_SECRET_KEY']


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello'


@app.route('/callback')
def callback():
    print(request)
    return 'test'


if __name__=='__main__':
    app.run(debug=True)