from random import shuffle
import json

class Question:
    """
    The Question class is intended for conducting a survey. Class attributes:
    "text_question" - contains the text of the question,
    "level_question" - contains information about the difficulty level of the question from 1 to 5,
    "right_answer" - contains the text of the correct answer to the question,
    "is_question_asked" - whether the question is asked (by default False),
    "users_answer" - the user's answer (by default None) and
    "points_for_answer" - points for the question (calculated at the time of initialization)
    """
    def __init__(self, text_question, level_question, right_answer):
        self.text_question = text_question
        self.level_question = level_question
        self.right_answer = right_answer
        self.is_question_asked = False
        self.users_answer = None
        self.points_for_answer = int(self.level_question[0]) * 10

    def get_points(self):
        """
        Returns int, the number of points. The points depend on the difficulty:
        10 points are given for 1, 50 points are given for 5.
        """
        return self.points_for_answer

    def is_correct(self):
        """
        Returns True if the user's response matches with the correct answer, otherwise False.
        """
        return self.right_answer == self.users_answer

    def build_question(self):
        """
        Returns the question in a way that the user understands.
        """
        return f'Вопрос: {self.text_question} \nСложность вопроса {self.level_question}/5'

    def build_feedback(self):
        """
        Returns the evaluation of the correctness of the answer in a way that the user understands
        """
        if self.is_correct():
            return f'Ответ верный, получено {self.points_for_answer} баллов'
        return f'Ответ неверный, верный ответ {self.right_answer}'


def load_questions():
    """
    The function reads the question data from an external file in JSON format formats
    and returns the data in the form of a Python dictionary.
    """
    with open('questions.json', 'r', encoding='utf-8') as file:
        file_json = file.read()
        file_dict = json.loads(file_json)
        return file_dict


def build_questions_object():
    """
    The function receives data, creates objects based on this data and returns them as a randomly shuffled list.
    """
    question_1, question_2, question_3, question_4, question_5 = None, None, None, None, None
    questions = [question_1, question_2, question_3, question_4, question_5]
    questions_data = load_questions()
    for i, dict_ in enumerate(questions_data):
        questions[i] = Question(dict_["q"], dict_["d"], dict_["a"])
    shuffle(questions)
    return questions


def processing_statistics(questions: list):
    """
    The function takes a list of objects as an argument, calculates the statistics
    of the survey and outputs the result.
    """
    score, counter_right = 0, 0
    for item in questions:
        if item.is_question_asked:
            if item.is_correct():
                score += item.points_for_answer
                counter_right += 1

    print('Вот и всё!')
    print(f'Отвечено {counter_right} вопроса из {len(questions)}')
    print(f'Набрано баллов: {score}')


def main():
    """
    The wrapper function ensures consistent execution of all code functions.
    """
    print('Игра начинается!')
    print()
    questions = build_questions_object()

    for item in questions:
        print(item.build_question())
        item.is_question_asked = True
        item.users_answer = input()
        print(item.build_feedback())
        print()

    processing_statistics(questions)


if __name__ == '__main__':
    main()
