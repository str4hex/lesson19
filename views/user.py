from flask import request
from flask_restx import Resource, Namespace
from implemented import user_service


ns_user = Namespace('users')

@ns_user.route('/')
class UserView(Resource):

    def post(self):
        user_json = request.json
        user_service.user_create(user_json)
        return 'the user has been successfully created', 204

@ns_user.route('/<int:uid>')
class UserViewId(Resource):

    def delete(self, uid):
        return user_service.delete_user(uid)

    def put(self, uid):
        user_json = request.json
        if "id" not in user_json:
            user_json['id'] = uid
        return user_service.update_user(user_json)