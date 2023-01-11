from flask_restx import Resource, Namespace

from dao.model.genre import GenreSchema

genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):

    def get(self):
        all_genres = genre_service.get_all()
        return genres_schema.dump(all_genres)


@genre_ns.route('/<int:did>')
class GenreView(Resource):

    def get(self, did: int):
        genre = genre_sevice.get_one(did)
        return genre_schema.dump(genre)