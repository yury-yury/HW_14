import json


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
    in the form of a string formatted in the specified form.
    """
    data = load_candidates_from_json('candidates.json')
    res = f'<h1>Все кандидаты</h1>'

    for dict_ in data:
        res += f"<p><a href='/candidate/{dict_['id']}'>{dict_['name']}</a></p>"

    return res



def get_candidate(candidate_id: int):
    """
    The function takes the candidate number as an argument and returns the candidate data in the specified
    formatted form as a string. If a candidate with such a number is not in the database,
    it returns the corresponding message.
    """
    data = load_candidates_from_json('candidates.json')

    for dict_ in data:
        if dict_['id'] == candidate_id:
            return f"<h1>{dict_['name']}</h1><p>{dict_['position']}</p><img src='{dict_['picture']}' width=200/>" \
                   f"<p>{dict_['skills']}</p>"

    return '<pre><h1 style="color:red">  В базе данных нет кандидата с таким номером</h1></pre>'


def get_candidates_by_name(candidate_name: str):
    """
    The function takes as an argument a part of the candidate's name and when called returns a list
    of all candidates whose name matches the desired value, in the form of a string formatted in the specified
    form. If there are no such candidates, the function returns the corresponding message in the specified format.
    """
    count_candidates, search = 0, ''

    candidate_name = candidate_name.lower()

    data = load_candidates_from_json('candidates.json')

    for dict_ in data:
        name = dict_['name'].lower()
        if candidate_name in name:
            count_candidates += 1
            search += f"<p><a href='/candidate/{dict_['id']}'>{dict_['name']}</a></p>"

    res = f'<h1>найдено кандидатов {count_candidates}</h2>'
    res += search

    if count_candidates:
        return res

    return '<pre><h1 style="color:red">  В базе данных нет кандидатов с таким именем</h1></pre>'


def get_candidates_by_skill(skill_name: str):
    """
    The function takes as an argument the required skill of the candidate and, when called, returns a list
    of all candidates with the required skill, in the form of a string formatted in the specified form.
    If there are no such candidates, the function returns the corresponding message in the specified format.
    """
    count_candidates, search = 0, ''

    candidate_skill = skill_name.lower()

    data = load_candidates_from_json('candidates.json')

    for dict_ in data:
        skills = dict_['skills'].lower()
        skills = skills.split(', ')
        if candidate_skill in skills:
            count_candidates += 1
            search += f"<p><a href='/candidate/{dict_['id']}'>{dict_['name']}</a></p>"

    res = f'<h1>Найдено с навыком {candidate_skill}: {count_candidates}</h2>'
    res += search

    if count_candidates:
        return res

    return '<pre><h1 style="color:red">  В базе данных нет кандидатов с такими навыками</h1></pre>'


#   Code for checking the functionality of the functions.
if __name__ == '__main__':

    #print(load_candidates_from_json('candidates.json'))
    #print(get_all())
    #print(get_candidate(5)
    #print(get_candidates_by_name('a')
    print(get_candidates_by_skill('python'))