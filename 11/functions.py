import json

from flask import template_rendered


def load_candidates_from_json(path: str):
    """
    The function takes as an argument the path to a file containing a database of candidates in JSON format,
    and returns candidate data in the form of a list of dictionaries.
    """
    with open(f'{path}', 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def get_all():
    """
    The function does not accept any arguments and when called returns a list of all candidates
    in the form of a list of dictionaries with personal data of all candidates.
    """
    data = load_candidates_from_json('candidates.json')
    return data


def get_candidate(candidate_id: int):
    """
    The function takes the candidate's personal number as an argument and returns the candidate's data
    in the form of a dictionary.
    """
    data = load_candidates_from_json('candidates.json')

    for dict_ in data:
        if dict_['id'] == candidate_id:
            return dict_


def get_candidates_by_name(candidate_name: str):
    """
    The function takes part of the candidate's name as an argument and returns a list when called
    of all the candidates whose names contain a given sequence of letters, the case of the characters does not matter.
    """
    search = []

    candidate_name = candidate_name.lower()

    data = load_candidates_from_json('candidates.json')

    for dict_ in data:
        name = dict_['name'].lower()
        if candidate_name in name:
            search.append(dict_)

    return search


def get_candidates_by_skill(skill_name: str):
    """
    The function takes as an argument the required skill of the candidate and returns a list when called
    of all candidates with the required skills, in the form of a dictionary containing personal data.
    """
    search = []

    candidate_skill = skill_name.lower()

    data = load_candidates_from_json('candidates.json')

    for dict_ in data:
        skills = dict_['skills'].lower()
        skills = skills.split(', ')
        if candidate_skill in skills:
            search.append(dict_)

    return search


#   Code for checking the functionality of the functions.
if __name__ == '__main__':

    #print(load_candidates_from_json('candidates.json'))
    #print(get_all())
    #print(get_candidate(5)
    #print(get_candidates_by_name('a')
    print(get_candidates_by_skill('python'))