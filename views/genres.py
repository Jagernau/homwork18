from flask_restx import Resource, Namespace

genres_ns = Namespace('genres')


@genres_ns.route('/')
class GenresView(Resource):
    def get(self):
        return "", 200



@genres_ns.route('/<init:gid>')
class GenreView(Resource):
    def get(self, gid):
        return "", 200

