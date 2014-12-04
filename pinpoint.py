import os
import base64

import requests
import json

from flask import Flask, request, jsonify, render_template
from urllib import quote_plus


CONSUMER_KEY = os.environ['APP_KEY']
CONSUMER_SECRET = os.environ['APP_SECRET']
CONSUMER_SECRET_KEY = os.environ['APP_SECRET_KEY']
API_KEY = os.environ['API_KEY']

app = Flask(__name__)


@app.route('/test')
def index():
    bearer_token_credentials = create_bearer_credentials(CONSUMER_KEY, CONSUMER_SECRET)
    bearer_token = get_bearer_token(bearer_token_credentials)
    
    resp = requests.get('https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=twitterapi&count=1', headers={
        'Authorization': 'Bearer {}'.format(bearer_token),
        })
    
    resp_coord = resp.json()[0]['coordinates']
    
    lng = 150.644
    lat = - 34.397
    return render_template('pinpoint.html', lng=lng, lat=lat, resp=resp, test_coord = coord)
    

def create_bearer_credentials(consumer_key, consumer_secret):
    return base64_encode(':'.join([url_encode(consumer_key), url_encode(consumer_secret)]))


def get_bearer_token(credentials):
    response = requests.post('https://api.twitter.com/oauth2/token', headers={
        'Authorization': 'Basic {}'.format(credentials), 
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        },
    data={'grant_type': 'client_credentials'},
    )
    auth_data_dict = response.json()
    assert auth_data_dict['token_type'] == 'bearer'
    return auth_data_dict['access_token']


def base64_encode(string):
    return base64.urlsafe_b64encode(string)


def url_encode(string):
    return quote_plus(string)


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')

