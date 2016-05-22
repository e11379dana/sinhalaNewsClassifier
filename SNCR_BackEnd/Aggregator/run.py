import flask
from flask_restful import Api
from flask.ext.cors import CORS

from NewsList.index import *

app = flask.Flask(__name__)
api = Api(app)
CORS(app)
api.add_resource(main, '/<string:Category>', endpoint='/')

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)