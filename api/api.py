from flask import Flask, json
from flask.ext.mongoengine import MongoEngine
from flask_restful import Resource, Api

from config import HOST, MONGODB_SETTINGS

db = MongoEngine()
app = Flask('Bullets')
app.config['MONGODB_SETTINGS'] = MONGODB_SETTINGS
db.init_app(app)
api = Api(app)

class User(db.Document):
    name = db.StringField(max_length=70)
    email = db.EmailField(required=True)
    role = db.StringField(max_length=50, required=True, default='User')
    groups = db.ListField()

class Group(db.Document):
    name = db.StringField(max_length=70, required=True)
    type = db.StringField(max_length=70, required=True)

class Entry(db.Document):
    name = db.StringField(max_length=70, required=True)
    secret = db.StringField(required=True)
    username = db.StringField(max_length=50)
    info = db.StringField()

class UserResource(Resource):
    def get(self):
        users = User.objects
        raw_data = []
        for data in users:
            raw_data.append(data.to_json())
        return raw_data

class HelloResource(Resource):
    def get(self):
        return {'name': 'bullets'}

api.add_resource(UserResource, '/user/')
api.add_resource(HelloResource, '/')

if __name__ == '__main__':
    app.run(host=HOST)
