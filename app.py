import os

from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy


from sqlalchemy.sql import func

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Area(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    areaname = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    areacode = db.Column(db.String(80), unique=True, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    desc = db.Column(db.Text)

    def __repr__(self):
        return f'<Area {self.areaname}>'