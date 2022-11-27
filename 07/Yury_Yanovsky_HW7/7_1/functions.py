import json

def load_data(arg:int):
    """
    The function takes the database number as an argument, reads data from an external file in JSON
    format, formats and returns data in the form of a Python dictionary.
    1 - data base 'students.json', 2 - data base 'professions.json'
    """
    with open('students.json' if arg == 1 else 'professions.json', 'r', encoding='utf-8') as file:
        file_json = file.read()
        file_dict = json.loads(file_json)
        return file_dict


def get_data(arg:int, key:int or str):
    """
    The function gets the database number and the value of the key being searched as arguments
    and returns the data in the form of a dictionary or None if this dictionary does not exist.
    1 - data base 'students.json', 2 - data base 'professions.json'
    """

    key_ = 'pk' if arg == 1 else 'title'
    data_base = load_data(arg)

    for dict_ in data_base:
        if dict_[key_] == key:
            return dict_
    return None


    #Code for checking the functionality of the functions.
if __name__ == '__main__':

    print(load_data (2))
    print(get_data(2, 'Frontend'))
    print(foolproof(1, 4))