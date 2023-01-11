from dao.model.movie import Movie


class MovieDAO:

    def __init__(self, session):
        self.session = session

    def get_all(self):
        print(self.session.query(Movie).all())
        return self.session.query(Movie).all()