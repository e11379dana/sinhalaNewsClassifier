import flask
from flask_restful import Api

from NewsList.index import *

app = flask.Flask(__name__)
api = Api(app)

api.add_resource(main, '/<string:Category>', endpoint='/')

if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)