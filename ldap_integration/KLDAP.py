from flask import Flask
import ldap
from flask import g
from flask import request
from flask import make_response
import os
import yaml

BASE_DIR = os.getcwd()

app = Flask(__name__)
app.debug = True

with open(os.path.join(BASE_DIR, '../config/app.yml'), 'r') as config_file:
    config_params = yaml.load(config_file)


def get_ldap_client():
    ldap_client = getattr(g, '_ldap_client', None)
    if ldap_client is None:
        ldap_client = g._ldap_client = init_ldap_client(config_params)
        ldap_client.set_option(ldap.OPT_REFERRALS, 0)
    return ldap_client


def init_ldap_client(config):
    ldap_client = ldap.initialize(config["LDAP_HOST"])
    return ldap_client


@app.route('/login', methods=['GET', 'POST'])
def ldap_login():
    if request.method == 'POST':
        form = request.form
        if "username" not in form or "password" not in form:
            return make_response(("", 401, {}))
        username = form["username"]
        password = form["password"]

        try:
            ldap_client = get_ldap_client()
            ldap_client.bind_s(username, password)
            return make_response(("", 200, {}))
        except BaseException:
            return make_response(("", 401, {}))


if __name__ == '__main__':
    app.run()
