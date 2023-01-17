from flask_restx import Resource, Namespace
from app.database import db
from app.models import MovieSchema, Movie
from flask import request

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesViews(Resource):
    def get(self, ):

        all_movies_ = db.session.query(Movie)
        director_id = request.args.get("director_id")
        genre_id = request.args.get("genre_id")
        year_id = request.args.get("year_id")
        if director_id:
            all_movies = all_movies_.filter(Movie.director_id == director_id)
            return movies_schema.dump(all_movies), 200
        if genre_id:
            all_movies = all_movies_.filter(Movie.genre_id == genre_id)
            return movies_schema.dump(all_movies), 200
        if year_id:
            all_movies = all_movies_.filter(Movie.year == year_id)
            return movies_schema.dump(all_movies), 200
        else:
            return movie_schema.dump(all_movies_)

    def post(self):
        try:
            req_json = request.json
            new_movie = Movie(**req_json)
            with db.session.begin():
                db.session.add(new_movie)
            return "", 201
        except Exception as e:
            return str(e)


@movie_ns.route('/<int:mid>')
class MoviesViews(Resource):
    def get(self, mid):

        movie = Movie.query.get(mid)
        return movie_schema.dump(movie)

    def put(self, mid: int):
        movie = Movie.query.get(mid)
        if not movie:
            return "", 404
        req_json = request.json
        movie.id = req_json.get("id")
        movie.title = req_json.get("title")
        movie.description = req_json.get("description")
        movie.trailer = req_json.get("trailer")
        movie.year = req_json.get("year")
        movie.rating = req_json.get("rating")
        movie.genre_id = req_json.get("genre_id")
        movie.director_id = req_json.get("director_id")
        db.session.add(movie)
        db.session.commit()
        return "", 204

    def delete(self, mid):
        movie = Movie.query.get(mid)
        if not movie:
            return "", 404
        db.session.delete(movie)
        db.session.commit()
