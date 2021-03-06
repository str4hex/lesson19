from flask import request
from flask_restx import Resource, Namespace, abort


from implemented import auth_service, user_service

ns_auth = Namespace('auth')


@ns_auth.route('/')
class AuthView(Resource):

    def post(self):
        req_json = request.json
        username = req_json.get('username')
        password = req_json.get('password')
        if not (username or password):
            return "Не задано имя или пароль", 400

        tokens = auth_service.generate_tokens(username, password)
        if tokens:
            return tokens
        else:
            return "Ошибка в запросе", 400


    def put(self):
        req_json = request.json
        refresh_token = req_json.get("refresh_token")
        if not refresh_token:
            return "Не задан токен", 400

        tokens = auth_service.refresh_token(refresh_token)
        if tokens:
            return tokens
        else:
            return "Ошибка в запросе", 400
