import json


def load_list_post():
    """
    The function does not accept any arguments. When called, loads all available posts from an external file
    and returns them as a list of dictionaries.
    """
    with open('posts.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def search_posts_by_tag(tag: str):
    """
    The function takes a string as an argument and, when called, searches for all posts whose description
    contains this string. Returns the search results as a list of dictionaries.
    """
    data = load_list_post()
    res = []

    for dict_ in data:
        search_str = dict_['content'].lower()
        if tag in search_str:
            res.append(dict_)

    return res
