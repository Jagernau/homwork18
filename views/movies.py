from flask import request
from flask_restx import Resource, Namespace
from implemented import movie_service
from dao.model.movies import MovieSchema

movie_ns = Namespace('movies')



@movie_ns.route("/")
class MoviesView(Resource):

    def get(self):
        schema = MovieSchema(many=True)

        return schema.dump(movie_service.get_movies(**request.args)), 200

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
        return movie_service.update_movie_full(movie_id, request.json)   

    def delete(self, movie_id):
        movie_service.delete(movie_id)
        return "", 204
