import json


def load_candidates():
    """
    The function does not accept arguments. When called, loads data from an external file
    and returns it as a dictionary.
    """
    with open('candidates.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

        return data


def display_candidat(candidat: dict):
    """
    The function takes as an argument the candidate data in the form of a dictionary
    and returns them in the specified formatted form as a string.
    """
    return (f"<pre><h3>\n  Имя кандидата - {candidat['name']}\n  Позиция кандидата - {candidat['position']}"
            f"\n  Навыки кандидата - {candidat['skills']}\n</h3></pre>")


def get_all():
    """
    The function does not accept arguments. When called, it returns the data of all candidates
    in the specified formatted form as a string.
    """
    data = load_candidates()
    res = ''

    for item in data:
        res += display_candidat(item)
    return res


def get_by_pk(pk: int):
    """
    The function takes the candidate number as an argument and returns the candidate data in the specified
    formatted form as a string. If a candidate with such a number is not in the database,
    it returns the corresponding message.
    """
    data = load_candidates()

    for dict_ in data:
        if dict_['pk'] == pk:
            return f"<img src={dict_['picture']}>" + display_candidat(dict_)

    return '<pre><h3>  В базе данных нет кандидата с таким номером</h3></pre>'


def get_by_skill(skill_name):
    """
    The function takes as an argument the required skill of candidates and returns the data of candidates
    having this skill in the specified formatted form as a string. If there are no candidates with this
    skill in the database, returns the corresponding message.
    """
    skill_name = skill_name.lower()
    data = load_candidates()
    res = ''

    for dict_ in data:
        #   Here is a string with data about the skills of the candidate in the format for the search
        skill_list = dict_['skills'].lower()
        skill_list = skill_list.split(', ')

        if skill_name in skill_list:
            res += display_candidat(dict_)

    if not res:
        return '<pre><h3>  В базе данных нет кандидатов с необходимыми навыками</h3></pre>'

    return res

#   Code for checking the functionality of functions
if __name__ == '__main__':

    #print(load_candidates())
    #print(get_all())
    #print(get_by_pk(2))
    print(get_by_skill('python'))
