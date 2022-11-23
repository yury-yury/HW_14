import json

def load_students():
    """
    The function reads data on students' professional skills from an external file in JSON
    format and returns data in the form of a Python dictionary.
    """
    with open('students.json', 'r', encoding='utf-8') as file:
        file_json = file.read()
        file_dict = json.loads(file_json)
        return file_dict


def get_student_by_pk(n:int):
    """
     The function receives the student's serial number and returns his personal data
     in the form of a dictionary.
    """
    students = load_students()
    for student in students:
        if student['pk'] == n:
            return student


def student_foolproof(n: int):
    """
    The function takes the student's number as an argument, and returns True if there
    is information in the database, otherwise False.
    """
    student_number_list = []
    for student in load_students():
        student_number_list.append(student['pk'])
    if n in student_number_list: return True
    return False


    #   Code for checking the functionality of the functions.
if __name__ == '__main__':

    print(load_students())
    print(get_student_by_pk(1))
    print(student_foolproof(5))