from flask import Flask, json
from flask.ext.mongoengine import MongoEngine
from flask_restful import Resource, Api, reqparse

from config import HOST, MONGODB_SETTINGS

db = MongoEngine()
app = Flask('Bullets')
app.config['MONGODB_SETTINGS'] = MONGODB_SETTINGS
db.init_app(app)
api = Api(app)
parser = reqparse.RequestParser()

class Person(db.Document):
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

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('email', action='append')
parser.add_argument('role', action='append')

class PersonResource(Resource):

    def get(self):
        data_objects = Person.objects
        return raw_data(data_objects)

    def post(self):
        args = parser.parse_args()
        try:
            person_id = Person(
                name=args['name'], role=args['role'], email=args['email']).save()
        except Exception as e:
            return {'message': "Error: {0}".format(e)}

        return {'message': 'OK'}

class GroupResource(Resource):
    def get(self):
        data_objects = Group.objects
        return raw_data(data_objects)

    def post(self):
        pass

class EntryResource(Resource):
    def get(self):
        data_objects = Entry.objects
        return raw_data(data_objects)

class HelloResource(Resource):
    def get(self):
        return {'name': 'bullets'}

def raw_data(data_objects):
    raw_data = []
    for data in data_objects:
        raw_data.append(data.to_json())
    return raw_data

api.add_resource(PersonResource, '/person/')
api.add_resource(GroupResource, '/group/')
api.add_resource(EntryResource, '/entry/')
api.add_resource(HelloResource, '/')

if __name__ == '__main__':
    app.run(host=HOST)
