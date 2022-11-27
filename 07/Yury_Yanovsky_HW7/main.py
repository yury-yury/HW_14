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


print('Введите номер студента')
n = int(input())

if not student_foolproof(n):
    print('У нас нет такого студента')
else:
    student = get_student_by_pk(n)
    print(f"Студент {student['full_name']}")
    print("Знает:", end=' ')
    output = ''
    for i in student['skills']:
        output += i + ', '
    print(output[ :-2])

    print()
    print(f"Выберите специальность для оценки студента {student['full_name']}")
    title = input().title()

    if not professions_foolproof(title):
        print('У нас нет такой специальности')
    else:
        result = check_fitness(student, get_profession_by_title(title))
        print(f"Пригодность {result['fit_percent']}%")
        print(f"{student['full_name']} знает:", end=' ')
        output = ', '
        for skill in result['has']:
            output += skill + ', '
        print(output[ :-2])
        print(f"{student['full_name']} не знает:", end=' ')
        output = ''
        for skill in result['lacks']:
            output += skill + ', '
        print(output[ :-2])
