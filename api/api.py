from flask import Flask, json
from flask.ext.mongoengine import MongoEngine
from flask_restful import Resource, Api

from config import HOST, MONGODB_SETTINGS, LDAP_HOST, APP_SECRET_KEY

db = MongoEngine()
app = Flask('Bullets')
app.config['MONGODB_SETTINGS'] = MONGODB_SETTINGS
app.secret_key = APP_SECRET_KEY
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

## LDAP
import ldap
from flask import g, request, session, Flask, redirect
from flask import make_response


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


if __name__ == '__main__':
    app.run(host=HOST)
