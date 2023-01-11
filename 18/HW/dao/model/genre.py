from marshmallow import Schema, fields

from setup_db import db


class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    movie = db.relationship('Movie')


class GenreSchema(Schema):
    id = fields.Int()
    name = fields.Str()

