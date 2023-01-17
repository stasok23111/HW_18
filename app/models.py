from app.database import db
from marshmallow import Schema, fields


class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    trailer = db.Column(db.String(255))
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"))
    genre = db.relationship("Genre")
    director_id = db.Column(db.Integer, db.ForeignKey("director.id"))
    director = db.relationship("Director")

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'trailer': self.title,
            'year': self.year,
            'rating': self.rating,
            'genre_id': self.genre_id,
            'director_id': self.director_id,
        }

class MovieSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
    genre_id = fields.Int()
    director_id = fields.Int()



class Director(db.Model):
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
        }

class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()





class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
        }




class GenreSchema(Schema):
    id = fields.Int()
    name = fields.Str()


