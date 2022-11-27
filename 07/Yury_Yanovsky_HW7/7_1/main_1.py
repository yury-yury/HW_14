from functions import get_data, foolproof


def check_fitness(student: dict, profession: dict):
    """
    The function receives the student's personal data and the data necessary for professional activity
    in the form of dictionaries and returns the result of the qualification check in the form of a dictionary.
    """
    student_skill = set(student['skills'])
    profession_skill = set(profession['skills'])

    has = list(student_skill.intersection(profession_skill))
    lacks = list(profession_skill.difference(student_skill))
    fit_percent = round(len(has) / len(profession_skill) * 100)

    return {'has': has, 'lacks': lacks, 'fit_percent': fit_percent}


def request_input(context:int, student: dict):
    """
    The function takes the context number as an argument requests input data
    from the user and returns it as an integer or string
    1 - request number of student, 2 - request name of profession
    """
    if context == 1:
        print('Введите номер студента')
        return int(input())

    elif context == 2:
        print(f"Выберите специальность для оценки студента {student['full_name']}")
        return input().title()


def student_data_output(student: dict):
    """
    The function accepts student data in the form of a dictionary and outputs them in a specified format
    """
    print()
    print(f"Студент {student['full_name']}")
    print("Знает:", end=' ')

    output = []
    for i in student['skills']:
        output.append(i)

    print(', '.join(output))
    print()


def output_result_check(result: dict, student: dict):
    """
    The function takes the results of the assessment of the student's suitability for the profession
    and the student's personal data in the form of dictionaries and outputs them in a given format.
    """
    print()
    print(f"Пригодность {result['fit_percent']}%")
    print(f"{student['full_name']} знает:", end=' ')

    output = []
    for skill in result['has']:
        output.append(skill)
    print(', '.join(output))

    print(f"{student['full_name']} не знает:", end=' ')

    output = []
    for skill in result['lacks']:
        output.append(skill)
    print(', '.join(output))


def main():
    """
    The wrapper function ensures the consistent functioning of the code
    """
    student = {}
    n = request_input(1, student)

    student = get_data(1, n)
    if student is None:
        print('У нас нет такого студента')
        return

    student_data_output(student)

    title = request_input(2, student)

    profession = get_data(2, title)
    if profession is None:
        print('У нас нет такой специальности')
        return

    output_result_check(check_fitness(student, profession), student)


if __name__ == "__main__":
    main()
    #print(request_input(2, {"pk": 1, "full_name": "Jane Snake", "skills": ["Python", "Go", "Linux"]}))
