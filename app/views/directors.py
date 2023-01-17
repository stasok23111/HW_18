from flask_restx import Resource, Namespace
from app.database import db
from app.models import DirectorSchema, Director, Movie, MovieSchema

directors_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

@directors_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        try:
            all_directors = db.session.query(Director).all()
            return directors_schema.dump(all_directors), 200
        except Exception as e:
            return str(e)



@directors_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did):
        director = Director.query.get(did)
        if not director:
            return "Not Found", 404
        all_movies = db.session.query(Movie).all()
        movie_in_director = []
        for i in all_movies:
            if i.genre_id == did:
                movie_in_director.append(movie_schema.dump(i))
        return [director_schema.dump(director), movie_in_director], 200


