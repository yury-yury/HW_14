import requests
import json
from random import sample


def load_words():
    """
    The function does not accept any arguments, when called, it requests data from an external resource
    and returns a random set of data in the form of a dictionary.
    """
    response = requests.get("https://www.jsonkeeper.com/b/NOHV")
    words = response.text
    words = json.loads(words)
    return sample(words, 1)[0]


def suffix_definition(cnt):
    """
    The function takes as an argument an integer number and returns the suffix of the word "слов" as a string.
    """
    if 5 <= cnt % 100 <= 20:
        return ''
    elif cnt % 10 == 1:
        return 'о'
    elif 2 <= cnt % 10 < 5:
        return 'а'
    return ''



if __name__ == '__main__':
    #https://jsonkeeper.com/b/NOHV
    print(load_words())
