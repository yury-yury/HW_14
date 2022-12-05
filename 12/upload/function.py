import json

from search.function import load_list_post


def add_post(dict_: dict):
    """
    The function takes as an argument a new post in the form of a dictionary and adds it to the list of posts.
    The function returns nothing.
    """
    data = load_list_post()
    data.append(dict_)

    with open('posts.json', 'w', encoding='utf-8') as file:
        json.dump(data, file)