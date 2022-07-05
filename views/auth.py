from flask import request
from flask_restx import Resource, Namespace, abort

ns_auth = Namespace('auth')


@ns_auth.route('/')
class AuthView(Resource):
    def post(self):
        pass

    def put(self):
        pass