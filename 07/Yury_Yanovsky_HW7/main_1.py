from utils import get_student_by_pk, student_foolproof
from functions import get_profession_by_title, professions_foolproof


def check_fitness(student: dict, profession: dict):
    """
    The function receives the student's personal data and the data necessary for professional activity
    in the form of dictionaries and returns the result of the qualification check in the form of a dictionary.
    """
    student_skill = student['skills']
    profession_skill = profession['skills']
    has = list(set(student_skill).intersection(set(profession_skill)))
    lacks = list(set(profession_skill).difference(set(student_skill)))
    fit_percent = round(len(has) / len(profession_skill) * 100)
    return {'has': has, 'lacks': lacks, 'fit_percent': fit_percent}


def request_student():
    """
    The function asks the user for the student's number and returns it as an integer
    """
    print('Введите номер студента')
    return int(input())


def student_data_output(student: dict):
    """
    The function accepts student data in the form of a dictionary and outputs them in a specified format
    """
    print()
    print(f"Студент {student['full_name']}")
    print("Знает:", end=' ')
    output = ''
    for i in student['skills']:
        output += i + ', '
    print(output[:-2])
    print()


def request_profession(student: dict):
    """
    The function executes the user's request about the profession for the student's
    assessment and returns the result of the request as a string.
    """
    print(f"Выберите специальность для оценки студента {student['full_name']}")
    return input().title()


def output_result_check(result: dict, student: dict):
    """
    The function takes the results of the assessment of the student's suitability for the profession
    and the student's personal data in the form of dictionaries and outputs them in a given format.
    """
    print()
    print(f"Пригодность {result['fit_percent']}%")
    print(f"{student['full_name']} знает:", end=' ')
    output = ', '
    for skill in result['has']:
        output += skill + ', '
    print(output[:-2])
    print(f"{student['full_name']} не знает:", end=' ')
    output = ''
    for skill in result['lacks']:
        output += skill + ', '
    print(output[:-2])


def main():
    """
    The wrapper function ensures the consistent functioning of the code
    """
    n = request_student()
    if not student_foolproof(n):
        print('У нас нет такого студента')
        return
    student = get_student_by_pk(n)
    student_data_output(student)
    title = request_profession(student)
    if not professions_foolproof(title):
        print('У нас нет такой специальности')
        return
    output_result_check(check_fitness(student, get_profession_by_title(title)), student)


if __name__ == "__main__":
    main()
