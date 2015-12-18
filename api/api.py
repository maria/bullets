import json

import ldap
from flask import Flask, json, request, session, redirect, make_response, g
from flask.ext.mongoengine import MongoEngine
from flask_restful import Resource, Api, reqparse

from config import HOST, MONGODB_SETTINGS, LDAP_HOST, APP_SECRET_KEY

db = MongoEngine()
app = Flask('Bullets')
app.config['MONGODB_SETTINGS'] = MONGODB_SETTINGS
app.secret_key = APP_SECRET_KEY
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
    group = db.StringField()


class PersonResource(Resource):
    def get(self, person_id):
        data_object = Person.objects.get_or_404(id=person_id)
        return raw_object(data_object)


class PersonsResource(Resource):

    def get(self):
        data_objects = Person.objects
        return raw_data(data_objects)

    def post(self):
        parser.add_argument('name', type=str)
        parser.add_argument('email', type=str)
        parser.add_argument('role', type=str)
        parser.add_argument('groups', type=list)
        args = parser.parse_args()

        try:
            person = Person(
                name=args['name'], role=args['role'], email=args['email'],
                groups=args['groups']).save()
        except Exception as e:
            return {'message': "Error: {0}".format(e)}

        return raw_object(person)


class GroupResource(Resource):
    def get(self, group_id):
        data_object = Group.objects.get_or_404(id=group_id)
        return raw_object(data_object)


class GroupsResource(Resource):
    def get(self):
        data_objects = Group.objects
        return raw_data(data_objects)

    def post(self):
        parser.add_argument('name', type=str)
        parser.add_argument('type', type=str)
        args = parser.parse_args()

        try:
            group = Group(name=args['name'], type=args['type']).save()
        except Exception as e:
            return {'message': "Error: {0}".format(e)}

        return raw_object(group)


class EntryResource(Resource):
    def get(self, entry_id):
        data_object = Entry.objects.get_or_404(id=entry_id)
        return raw_object(data_object)


class EntriesResource(Resource):
    def get(self):
        data_objects = Entry.objects
        return raw_data(data_objects)

    def post(self):
        parser.add_argument('name', type=str)
        parser.add_argument('secret', type=str)
        parser.add_argument('info', type=str)
        parser.add_argument('group', type=str)
        args = parser.parse_args()

        try:
            entry = Entry(
                name=args['name'], secret=args['secret'],
                group=args['group'], info=args.get('info')).save()

        except Exception as e:
            return {'message': "Error: {0}".format(e)}

        return raw_object(entry)


def raw_object(data_object):
    data = json.loads(data_object.to_json())
    data['id'] = data['_id']['$oid']
    data.pop('_id')
    return data


def raw_data(data_objects):
    raw_data = []
    for data in data_objects:
        data = json.loads(data.to_json())
        data['id'] = data['_id']['$oid']
        data.pop('_id')
        raw_data.append(data)
    return raw_data

## LDAP
def get_ldap_client():
    ldap_client = getattr(g, '_ldap_client', None)
    if ldap_client is None:
        ldap_client = g._ldap_client = init_ldap_client()
        ldap_client.set_option(ldap.OPT_REFERRALS, 0)
    return ldap_client


def init_ldap_client():
    ldap_client = ldap.initialize(LDAP_HOST)
    return ldap_client


@app.route('/')
def index():
    if 'username' not in session:
        return redirect('login')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        form = request.form
        if 'username' not in form or 'password' not in form:
            return make_response(('', 400, {}))
        username = form['username']
        password = form['password']

        username = username.replace('@kalon.ro', '@ad.kalon.ro')

        try:
            ldap_client = get_ldap_client()
            ldap_client.bind_s(username, password)
            session.pop('username', None)
            session['username'] = username
            return redirect('/')
        except BaseException:
            return make_response(('', 401, {}))
    return '''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=password name=password>
            <p><input type=submit value=Login>
        </form>
    '''


@app.route('/logout', methods=['DELETE'])
def logout():
    if 'username' in session:
        session.pop('username', None)
    return redirect('/')


api.add_resource(PersonResource, '/person/<person_id>')
api.add_resource(PersonsResource, '/person/')
api.add_resource(GroupResource, '/group/<group_id>')
api.add_resource(GroupsResource, '/group/')
api.add_resource(EntryResource, '/entry/<entry_id>')
api.add_resource(EntriesResource, '/entry/')

if __name__ == '__main__':
    app.run(host=HOST, debug=True)
