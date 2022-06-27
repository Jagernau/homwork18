from flask_restx import Resource, Namespace

directors_ns = Namespace('directors')


@directors_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        return "", 200



@directors_ns.route('/<init:did>')
class DirectorView(Resource):
    def get(self, did):
        return "", 200

