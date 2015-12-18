from flask import Flask
from flask.ext.mongoengine import MongoEngine
from flask_restful import Resource, Api

from config import HOST

db = MongoEngine()
app = Flask('Bullets')
app.config.from_pyfile('config.py')
db.init_app(app)
api = Api(app)

class HelloResource(Resource):
    def get(self):
        return {'name': 'bullets'}

api.add_resource(HelloResource, '/')

if __name__ == '__main__':
    app.run(host=HOST)
