"""Configures app, database and Marshmallow"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Flask config
app = Flask(__name__)

# Sqlite config
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///site.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Sqlalchemy config
db = SQLAlchemy(app)

# Marchmallow config
ma = Marshmallow(app)