import ldap
from flask import g, request, session, Flask, redirect
from flask import make_response
import os
import yaml

BASE_DIR = os.getcwd()

app = Flask(__name__)
app.debug = True

with open(os.path.join(BASE_DIR, '../config/app.yml'), 'r') as config_file:
    config_params = yaml.load(config_file)
    app.secret_key = config_params['APP_SECRET_KEY']


def get_ldap_client():
    ldap_client = getattr(g, '_ldap_client', None)
    if ldap_client is None:
        ldap_client = g._ldap_client = init_ldap_client(config_params)
        ldap_client.set_option(ldap.OPT_REFERRALS, 0)
    return ldap_client


def init_ldap_client(config):
    ldap_client = ldap.initialize(config['LDAP_HOST'])
    return ldap_client


@app.route('/')
def index():
    if 'username' not in session:
        return redirect('login')
    return '''<span> Success </span>'''


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


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if 'username' in session:
        session.pop('username', None)
    return redirect('/')


if __name__ == '__main__':
    app.run()
