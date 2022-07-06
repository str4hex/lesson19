from flask import request
from flask_restx import Resource, Namespace, abort

from dao.model.director import DirectorSchema
from implemented import director_service

director_ns = Namespace('directors')


@director_ns.route('')
class DirectorsView(Resource):
    def get(self):
        rs = director_service.get_all()
        res = DirectorSchema(many=True).dump(rs)
        return res, 200

    def post(self):
        reg_json = request.json
        director = director_service.create(reg_json)
        return "", 201


@director_ns.route('/<int:rid>')
class DirectorView(Resource):
    def get(self, rid):
        r = director_service.get_one(rid)
        sm_d = DirectorSchema().dump(r)
        return sm_d, 200

    def put(self, rid):
        reg_json = request.json
        if "id" not in reg_json:
            reg_json["id"] = rid
        director_service.update(reg_json)
        return '', 204

    def delete(self, rid):
        return director_service.delete(rid), 201
