from flask import request
from flask_restx import Resource, Namespace
from ..implemented import movie_service


movie_ns = Namespace('movies')


@movie_ns.route("/")
class MoviesView(Resource):
    def get(self):
        return movie_service.get_movies()

    def post(self):
        new_movie = movie_service.create_movie(request.json)
        return "", 201, {'location: f"{movie_ns.patch}/{new_movie.id}"'}


@movie_ns.route("/<int:movie_id>")
class MovieView(Resource):
    def get(self, movie_id: int):       
        return movie_service.get_movies(movie_id)

    def patch(self, movie_id: int):
        return movie_service.update_movie_partial(movie_id, request.json)



    def put(self, movie_id):        
        movie = db.session.query(Movie).filter(Movie.id==movie_id).first()
        req_json = request.json
        movie.title = req_json['title']
        movie.description = req_json['description']
        movie.trailer = req_json['trailer']
        movie.year = req_json['year']
        movie.rating = req_json['rating']
        movie.genre_id = req_json['genre_id']
        movie.director_id = req_json['director_id']
        db.session.add(movie)
        db.session.commit()
        return f"Объект с id {movie_id} обновлён!", 204
    

    def delete(self, movie_id):
        try:
            movie_service.delete(movie_id)
            return 204
        except Exception as e:
            print(e)
            return 500
