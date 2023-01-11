from flask import request
from flask_restx import Resource, Namespace

from dao.model.movie import MovieSchema
from implemented import movie_service

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):

    def get(self):

        if request.args.get("director_id"):
            movies = movie_service.get_all_by_director(request.args.get("director_id"))
            return movies_schema.dump(movies)

        elif request.args.get("genre_id"):
            movies = movie_service.get_all_by_genre(request.args.get("genre_id"))
            return movies_schema.dump(movies)

        elif request.args.get("year"):
            movies = movie_service.get_all_by_year(request.args.get("year"))
            return movies_schema.dump(movies)

        else:
            all_movies = movie_service.get_all()
            return movies_schema.dump(all_movies)

    def post(self):

        req_json = request.json
        movie = movie_service.create(req_json)
        return movie_schema.dump(movie)



@movie_ns.route('/<int:mid>')
class MovieView(Resource):

    def get(self, mid: int):
        movie = movie_service.get_one(mid)
        return movie_schema.dump(movie)

    def put(self, mid: int):
        req_json = request.json
        req_json["id"] = mid
        movie = movie_service.update(req_json)
        return movie_schema.dump(movie)

    def delete(self, mid: int):
        movie_service.delete(mid)
        return ""