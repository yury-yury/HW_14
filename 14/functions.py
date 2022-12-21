import sqlite3

import json

def make_data_film(title: str):
    """
    The function takes as an argument, the name of the movie as a string, makes a query from the database
    and returns the movie data in the form of a dictionary with the specified keys.
    If more than one movie is found, the data of the movie released last is returned.
    """
    res_dict = {"title": None, "country": None, "release_year": 0, "genre": None, "description": None}

    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()

        query = f"""
                SELECT title, country, release_year, listed_in, description
                FROM netflix
                WHERE title LIKE '%{str(title)}%'
                ORDER BY release_year DESC
                LIMIT 1
                """

        cursor.execute(query)
        res = cursor.fetchall()

        for item in res:
            res_dict["title"] = item[0]
            res_dict["country"] = item[1]
            res_dict["release_year"] = item[2]
            res_dict["genre"] = item[3]
            res_dict["description"] = item[4]

        return res_dict


def make_data_film_years(from_year: int, to_year: int):
    """
    The function takes as arguments the values of the years of release of films, in the form of integers,
    makes a query from the database and returns a list of dictionaries with data of films released between
    the specified years, sorted from late to early, in the amount of 100 pieces.
    """
    res_list = []

    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()

        query = f"""SELECT title, release_year
                    FROM netflix
                    WHERE release_year BETWEEN {from_year} AND {to_year}
                    AND type = 'Movie'
                    ORDER BY release_year DESC
                    LIMIT 100"""


        cursor.execute(query)
        res = cursor.fetchall()

        for item in res:
            res_list.append({"title": item[0], "release_year": item[1]})

        return res_list


def make_data_film_rating(*args: str):
    """
    The function takes one or more movie rating values as arguments, makes a query from an external database,
    sorts depending on the year of release and returns the data of the found movies in the form of a list
    of dictionaries. The length of the list is limited to one hundred films.
    """
    res_list = []

    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()

        query = f"""SELECT title, rating, description
                        FROM netflix
                        WHERE type = 'Movie'
                        AND """

        query_1 = []
        for arg in args:
            query_1.append(f"""rating = '{arg}'""")

        query += ' OR '.join(query_1) + f""" ORDER BY release_year DESC
                        LIMIT 100"""

        cursor.execute(query)
        res = cursor.fetchall()

        for item in res:
            res_list.append({"title": item[0], "rating": item[1], "description": item[2]})

        return res_list


def make_data_film_by_genre(genre: str):
    """
    The function takes as an argument the name of the genre of the movie, in the form of a string.
    Makes a query from an external database of all films, sorts them by year of release in order from
    fresh to old, and returns the ten most recent films corresponding to the requested genre in the form
    of a list of dictionaries containing movie data.
    """
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()

        query = f"""
                SELECT title, description
                FROM netflix
                WHERE listed_in LIKE '%{str(genre)}%'
                ORDER BY release_year DESC
                LIMIT 10
                """

        cursor.execute(query)
        res = cursor.fetchall()

        return res


def find_partners(name_1: str, name_2: str):
    """
    The function receives the names of two actors as arguments, in the form of strings, queries all the actors
    who played with them from the "cast" field of the external database, saves and returns a list of those
    who play with them in a pair more than 2 times.
    """
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()

        query = f"""
                SELECT "cast"
                FROM netflix
                WHERE "cast" LIKE '%{str(name_1)}%'
                AND "cast" LIKE '%{str(name_2)}%'
                """

        cursor.execute(query)
        res = cursor.fetchall()

    actor_list = []
    for item in res:
        actor_list.extend(item[0].split(', '))

    actor_set = set(actor_list)
    actor_set.discard(name_1)
    actor_set.discard(name_2)

    res = []
    for actor in actor_set:
        if actor_list.count(actor) > 2:
            res.append(actor)

    return res


def search_for_movies_by_characteristics(type: str, release_year: int, genre: str):
    """
    The function receives a set of values as arguments: the type of painting (movie or TV series) as a string,
    the year of release as an integer and its genre as a string, makes a query from an external database
    in accordance with the specified conditions and returns a list of the names of paintings with their
    descriptions in JSON.
    """
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()

        query = f"""
                    SELECT title, description
                    FROM netflix
                    WHERE type = '{type}'
                    AND listed_in LIKE '%{genre}%'
                    AND release_year = '{release_year}'
                    """

        cursor.execute(query)
        res = cursor.fetchall()

    res_list = []
    for item in res:
        dict_ = {}
        dict_['title'] = item[0]
        dict_['description'] = item[1]
        res_list.append(dict_)

    return json.dumps(res_list)



if __name__ == '__main__':

    #   Code for checking and configuring the functionality of functions.
    #print(make_data_film_years(2010, 2011))
    #print(make_data_film_rating('G', 'PG', 'PG-13'))
    #print(find_partners('Jack Black', 'Dustin Hoffman'))
    print(search_for_movies_by_characteristics('Movie', 2001, 'Dramas'))