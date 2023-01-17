from flask_restx import Resource, Namespace
from app.database import db
from app.models import GenreSchema, MovieSchema, Genre, Movie, Director

genres_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

@genres_ns.route('/')
class GenresView(Resource):
    def get(self):
        try:
            all_genres = db.session.query(Genre).all()
            return genres_schema.dump(all_genres), 200
        except Exception as e:
            return str(e)




@genres_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        genre = Genre.query.get(gid)
        if not genre:
            return "Not found", 404
        all_movies = db.session.query(Movie).all()
        movie_in_genre = []
        for i in all_movies:
            if i.genre_id == gid:
                movie_in_genre.append(movie_schema.dump(i))
        return [genre_schema.dump(genre), movie_in_genre], 200


