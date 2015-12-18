from flask import Flask
from flask.ext.mongoengine import MongoEngine

db = MongoEngine()
app = Flask('Bullets')
app.config.from_pyfile('config.py')
db.init_app(app)
