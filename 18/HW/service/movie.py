from dao.movie import MovieDAO


class MovieService:

    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_all_by_director(self, did: int):
        pass

    def get_all_by_genre(self, gid: int):
        pass

    def get_all_by_year(self, year: int):
        pass

    def get_all(self):
        return self.dao.get_all()

    def create(self, data: dict):
        pass

    def get_one(self, mid: int):
        pass

    def update(self, data: dict):
        pass

    def delete(self, mid: int):
        pass