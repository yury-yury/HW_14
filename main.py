from flask import Flask, jsonify, request

from functions import make_data_film, make_data_film_years, make_data_film_rating, make_data_film_by_genre


app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False


@app.route('/movie/<title>')
def view_film(title):
    """
    The view processes requests to the address /movie/<title>, extracts the value of the variable part
    of the address, uses an external function to get data and returns it as JSON.
    """
    return jsonify(make_data_film(title.title()))


@app.route('/movie/year/to/year')
def view_film_for_the_period():
    """
    The view processes requests at /movie/year/to/year, extracts the value of query parameters, using
    an external function, receives data and returns it as JSON.
    """
    year_from = int(request.values.get('from'))
    year_to = int(request.values.get('to'))

    return jsonify(make_data_film_years(year_from, year_to))


@app.route('/rating/<rating>')
def view_film_by_rating(rating):
    """
    The view processes requests at /rating/<rating>, extracts the value of the variable part of the address,
    depending on the value of the variable part of the address, forms a request to an external function,
    receives data from it and returns it as JSON.
    """
    if rating == 'children':
        res = make_data_film_rating('G')
    elif rating == 'family':
        res = make_data_film_rating('G', 'PG', 'PG-13')
    elif rating == 'adult':
        res = make_data_film_rating('R', 'NC-17')

    return jsonify(res)


@app.route('/genre/<genre>')
def view_film_by_genre(genre):
    """
    The view processes requests at /genre/<genre>, extracts the value of the variable part of the address,
    uses an external function to get data and returns it in JSON form.
    """
    return jsonify(make_data_film_by_genre(genre.title()))


if __name__ == '__main__':

    app.run(debug=True)
