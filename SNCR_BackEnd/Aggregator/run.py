import os
from httplib2 import Http

import flask
from flask_restful import Api
from flask.ext.cors import CORS
from urllib2 import Request, urlopen, URLError
from flask import session, redirect, url_for, json


from NewsList.index import *
from Authentication import *

app = flask.Flask(__name__)
app.secret_key = os.urandom(24)
api = Api(app)
CORS(app)
api.add_resource(main, '/<string:Category>', endpoint='/')
api.add_resource(Login, '/login')

def get_user_data(access_token):
    parser = Http()
    resp, content = parser.request("https://www.googleapis.com/oauth2/v1/userinfo?access_token={accessToken}".format(
        accessToken=access_token))
    # this gets the google profile!!
    print content
    return content

@app.route('/callback')
@google.authorized_handler
def authorized(resp):
    session['access_token'] = resp['access_token']
    return get_user_data(session["access_token"])


@google.tokengetter
def get_access_token():
    return session.get('access_token')

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)