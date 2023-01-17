from flask import Flask
from flask_restx import Api

from app.config import Config
from app.database import db
from app.models import Movie, Genre, Director
from app.views.directors import directors_ns
from app.views.genres import genres_ns
from app.views.movies import movie_ns


def create_app(config: Config) -> Flask:
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()

    return application


def configure_app(application: Flask):
    db.init_app(application)
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(directors_ns)
    api.add_namespace(genres_ns)


def load_data():
    movie_1 = Movie(id=1,
                    title='Test',
                    description='Test_1',
                    trailer='1243',
                    year=2023,
                    rating=9,
                    genre_id=1,
                    director_id=1)
    director_1 = Director(id=1,
                          name='Test')
    genre_1 = Genre(id=1,
                    name='Test_2')
    db.create_all()

    with db.session.begin():
        db.session.add_all([movie_1])
        db.session.add_all([director_1])
        db.session.add_all([genre_1])


if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)
    configure_app(app)
    load_data()
    app.run()
