import json

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


class PersonResource(Resource):
    def get(self, person_id):
        data_object = Person.objects.get_or_404(id=person_id)
        return json.loads(data_object.to_json())


class PersonsResource(Resource):

    def get(self):
        data_objects = Person.objects
        return raw_data(data_objects)

    def post(self):
        parser.add_argument('name', type=str)
        parser.add_argument('email', type=str)
        parser.add_argument('role', type=str)
        args = parser.parse_args()

        try:
            person_id = Person(
                name=args['name'], role=args['role'], email=args['email']).save()
        except Exception as e:
            return {'message': "Error: {0}".format(e)}

        return {'person_id': person_id}


class GroupResource(Resource):
    def get(self, group_id):
        data_object = Group.objects.get_or_404(id=group_id)
        return json.loads(data_object.to_json())


class GroupsResource(Resource):
    def get(self):
        data_objects = Group.objects
        return raw_data(data_objects)

    def post(self):
        parser.add_argument('name', type=str)
        parser.add_argument('type', type=str)
        args = parser.parse_args()

        try:
            group_id = Group(name=args['name'], type=args['type']).save()
        except Exception as e:
            return {'message': "Error: {0}".format(e)}

        return {'group_id': group_id}


class EntryResource(Resource):
    def get(self, entry_id):
        data_object = Entry.objects.get_or_404(id=entry_id)
        return json.loads(data_object.to_json())


class EntriesResource(Resource):
    def get(self):
        data_objects = Entry.objects
        return raw_data(data_objects)

    def post(self):
        parser.add_argument('name', type=str)
        parser.add_argument('secret', type=str)
        parser.add_argument('info', type=str)
        parser.add_argument('groups', type=str)
        args = parser.parse_args()

        groups = args['groups'].split(',')

        try:
            entry_id = Entry(
                name=args['name'], secret=args['secret'],
                info=args['info'], groups=groups).save()

        except Exception as e:
            return {'message': "Error: {0}".format(e)}

        return {'entry_id': entry_id}


def raw_data(data_objects):
    raw_data = []
    print data_objects
    for data in data_objects:
        raw_data.append(json.loads(data.to_json()))
    return raw_data


api.add_resource(PersonResource, '/person/<person_id>')
api.add_resource(PersonsResource, '/person/')
api.add_resource(GroupResource, '/group/<group_id>')
api.add_resource(GroupsResource, '/group/')
api.add_resource(EntryResource, '/entry/<entry_id>')
api.add_resource(EntriesResource, '/entry/')


if __name__ == '__main__':
    app.run(host=HOST)
