from flask_restful import Resource
from flask import *
from flask_oauth import OAuth

oauth = OAuth()

google = oauth.remote_app('google',
                          base_url='https://www.google.com/accounts/',
                          authorize_url='https://accounts.google.com/o/oauth2/auth',
                          request_token_url=None,
                          request_token_params={'scope': 'https://www.googleapis.com/auth/userinfo.email',
                                                'response_type': 'code'},
                          access_token_url='https://accounts.google.com/o/oauth2/token',
                          access_token_method='POST',
                          access_token_params={'grant_type': 'authorization_code'},
                          consumer_key="365664512462-2ck2v4j8f17s3rut6a1nd3s5cqfk193d.apps.googleusercontent.com",
                          consumer_secret="bNn-Kw5qUQj9_hE9dyX4cq6p")


class Login(Resource):
    def get(self):
        callback = url_for('authorized', _external=True)
        return google.authorize(callback=callback)