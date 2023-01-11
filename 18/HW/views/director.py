from flask_restx import Resource, Namespace

from dao.model.director import DirectorSchema

director_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)

@director_ns.route('/')
class DirectorsView(Resource):

    def get(self):
        all_directors = director_service.get_all()
        return directors_schema.dump(all_directors)


@director_ns.route('/<int:did>')
class DirectorView(Resource):

    def get(self, did: int):
        director = director_sevice.get_one(did)
        return director_schema.dump(director)