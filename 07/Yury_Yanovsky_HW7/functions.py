import json

def load_professions():
    """
    The function reads data on the professional skills of IT specialists from an external file in JSON
    format and returns data in the form of a Python dictionary.
    """
    with open('professions.json', 'r', encoding='utf-8') as file:
        file_json = file.read()
        file_dict = json.loads(file_json)
        return file_dict

def get_profession_by_title(title: str):
    """
    The function gets the name of the profession and returns its data about the profession
    in the form of a dictionary.
    """
    professions = load_professions()
    for profession in professions:
        if profession['title'] == title:
            return profession


def professions_foolproof(title: str):
    """
    The function takes as an argument the name of the profession, and returns True if there
    is information in the database, otherwise False
    """
    professions_list = []
    for profession in load_professions():
        professions_list.append(profession['title'])

    if title in professions_list: return True
    return False

    #   Code for checking the functionality of the functions.
if __name__ == '__main__':

    print(load_professions())
    print(get_profession_by_title('Backend'))
    print(professions_foolproof('Fullstack'))