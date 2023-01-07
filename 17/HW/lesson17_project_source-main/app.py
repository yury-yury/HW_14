# app.py

from flask import Flask, request, jsonify
from flask_restx import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_AS_ASCII'] = False
app.app_context().push()
db = SQLAlchemy(app)


class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    trailer = db.Column(db.String(255))
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"))
    genre = db.relationship("Genre")
    director_id = db.Column(db.Integer, db.ForeignKey("director.id"))
    director = db.relationship("Director")


class MovieSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str()
    description = fields.Str()
    year = fields.Int()
    trailer = fields.Str()
    rating = fields.Float()
    genre_id = fields.Int()
    director_id = fields.Int()


class Director(db.Model):
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()


class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class GenreSchema(Schema):
    id = fields.Int()
    name = fields.Str()


movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)

api = Api(app)
movie_ns = api.namespace('movies')
director_ns = api.namespace('directors')
genre_ns = api.namespace('genre')

@movie_ns.route('/')
class MoviesView(Resource):

    def get(self):
        if request.args.get("director_id") and request.args.get("genre_id"):
            movies = db.session.query(Movie).filter(Movie.director_id == int(request.args.get("director_id")),
                                                    Movie.genre_id == int(request.args.get("genre_id")))
            return movies_schema.dump(movies)

        elif request.args.get("director_id"):
            movies = db.session.query(Movie).filter(Movie.director_id == int(request.args.get("director_id")))
            return movies_schema.dump(movies)

        elif request.args.get("genre_id"):
            movies = db.session.query(Movie).filter(Movie.genre_id == int(request.args.get("genre_id")))
            return movies_schema.dump(movies)

        else:
            page = request.args.get("page", 1, type=int)
            all_movies = db.session.query(Movie).limit(2).offset((page - 1) * 2).all()
            return movies_schema.dump(all_movies)


    def post(self):
        movie = request.json

        movie_dict = movie_schema.load(movie)
        new_movie = Movie(**movie_dict)

        db.session.add(new_movie)
        db.session.commit()

        return movie_schema.dump(new_movie)


@movie_ns.route('/<int:mid>')
class MovieView(Resource):

    def get(self, mid: int):
        movie = db.session.query(Movie).get(mid)
        return movie_schema.dump(movie)

    def put(self, mid: int):
        movie = db.session.query(Movie).get(mid)
        update_movie = request.json

        movie.id = update_movie["id"]
        movie.title = update_movie["title"]
        movie.description = update_movie["description"]
        movie.trailer = update_movie["trailer"]
        movie.year = update_movie["year"]
        movie.rating = update_movie["rating"]
        movie.genre_id = update_movie["genre_id"]
        movie.director_id = update_movie["director_id"]

        db.session.add(movie)
        db.session.commit()

        return movie_schema.dump(movie)

    def delete(self, mid: int):
        movie = db.session.query(Movie).get(mid)

        db.session.delete(movie)
        db.session.commit()

        return ''


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        directors = db.session.query(Director).all()
        return directors_schema.dump(directors)

    def post(self):
        director = request.json

        director_dict = director_schema.load(director)
        new_director = Director(**director_dict)

        db.session.add(new_director)
        db.session.commit()

        return movie_schema.dump(new_director)


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did: int):
        director = db.session.query(Director).get(did)
        return director_schema.dump(director)

    def put(self, did: int):
        director = db.session.query(Director).get(did)
        director_update = request.json

        director.id = director_update["id"]
        director.name = director_update["name"]

        db.session.add(director)
        db.session.commit()

    def delete(self, did: int):
        director = db.session.query(Director).get(did)

        db.session.delete(director)
        db.session.commit()

        return ''


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        genres = db.session.query(Genre).all()
        return genres_schema.dump(genres)


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self,gid: int):
        genre = db.session.query(Genre).get(gid)
        movies = db.session.query(Movie).filter(Movie.genre_id == gid).all()
        movies_list = []
        for item in movies:
            movies_list.append(item.title)
        res = {"id": genre.id, "name": genre.name, "movies": movies_list}
        return jsonify(res)


if __name__ == '__main__':
    app.run(debug=True)
