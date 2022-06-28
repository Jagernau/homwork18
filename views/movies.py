from flask import make_response, request
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
        resp = make_response("", 201)
        resp.headers['location'] = f"{movie_ns.path}/{new_movie.id}"
        return resp



@movie_ns.route("/<int:movie_id>")
class MovieView(Resource):
    schema = MovieSchema()


    def get(self, movie_id: int):       
        return self.schema.dump(movie_service.get_movies(movie_id)), 200


    def patch(self, movie_id: int):
        return  self.schema.dump(movie_service.update_movie_partial(movie_id, request.json)), 200


    def put(self, movie_id):        
        return self.schema.dump(movie_service.update_movie_full(movie_id, request.json)), 200


    def delete(self, movie_id):
        movie_service.delete(movie_id)
        return "", 204
