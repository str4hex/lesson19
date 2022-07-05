import jwt
from flask import request
from flask_restx import Resource, Namespace, abort

from dao.model.director import DirectorSchema
from implemented import director_service

director_ns = Namespace('directors')


algo = 'HS256'
secret = 'wdfawf@ew332ref_3w'

datas = {
	"username:": "ok",
	"role": "user"
}

def auth_required(func):
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)
        data = request.headers['Authorization']
        token = data
        print(token)
        tokens = jwt.encode(datas, secret, algorithm=algo)
        print(tokens)
        try:
            jwt.decode(token, secret, algorithms=[algo])
        except Exception as e:
            print("JWT Decode Exception", e)
            abort(401)
        return func(*args, **kwargs)

    return wrapper


@director_ns.route('/')
class DirectorsView(Resource):
    @auth_required
    def get(self):
        rs = director_service.get_all()
        res = DirectorSchema(many=True).dump(rs)
        return res, 200

    def post(self):
        pass


@director_ns.route('/<int:rid>')
class DirectorView(Resource):
    def get(self, rid):
        r = director_service.get_one(rid)
        sm_d = DirectorSchema().dump(r)
        return sm_d, 200


    def put(self):
        pass

    def delete(self):
        pass