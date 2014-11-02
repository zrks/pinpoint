import os
from flask import Flask, request
import base64
from urllib import quote_plus


CONSUMER_KEY = os.environ['APP_KEY']
CONSUMER_SECRET = os.environ['APP_SECRET']
CONSUMER_SECRET_KEY = os.environ['APP_SECRET_KEY']


app = Flask(__name__)


@app.route('/')
def index():
    bearer_token_credentials = base64_encode(':'.join([url_encode(CONSUMER_KEY), url_encode(CONSUMER_SECRET)]))
    
    return bearer_token_credentials


@app.route('/callback')
def callback():
    print(request)
    return 'test'


def base64_encode(string):
    return base64.urlsafe_b64encode(string)


def url_encode(string):
    return quote_plus(string)


if __name__=='__main__':
    app.run(debug=True)