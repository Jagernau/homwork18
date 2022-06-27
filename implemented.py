from setup_db import db

from dao.movie import MovieDAO

from service.movie import MovieService


movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao)
