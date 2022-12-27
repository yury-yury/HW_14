from random import sample

words_list = ['person', 'man', 'woman', 'child', 'boy', 'girl', 'friend', 'name', 'single', 'age', 'old', 'young',
                'father', 'mother', 'wife', 'son', 'sister', 'uncle', 'aunt', 'nephew', 'niece', 'cousin', 'arm',
                'back', 'beard', 'bone', 'cheek', 'chest', 'chin', 'ear', 'elbow', 'eye', 'face', 'finger', 'foot',
                'hair', 'hand', 'head', 'heart', 'heel', 'knee', 'leg', 'lips', 'mouth', 'nail', 'neck', 'nose',
                'organ', 'skin', 'spine', 'throat', 'toe', 'tongue', 'tooth']

morse_dict = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....",
                "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.",
                "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
                "y": "-.--", "z": "--.."}

answers = []


def morse_encode(word):
    """
    The function takes as an argument a string of letters of the latin alphabet and returns a string
    of combinations of dots and dashes corresponding to the Morse code, the sequences corresponding
    to one letter are separated by a space.
    """
    result = ''
    word = word.lower()
    for i in word:
        result += morse_dict[i] + ' '
    return result[:-1]


def get_word():
    """
    When called, the function returns a random word from the words_list.
    """
    return sample(words_list, 1)[0]


def print_statistics(answers):
    """
    The function outputs the results of the passage based on the correctness of the user's answers.
    """
    print()
    print(f'Всего задачек: {len(answers)}')
    if answers.count(True) > 0:
        print(f'Отвечено верно: {answers.count(True)}')
    if answers.count(False) > 0:
        print(f'Отвечено неверно: {answers.count(False)}')


print('Сегодня мы потренируемся расшифровывать азбуку Морзе')
input('Нажмите Enter и начнем')

for i in range(5):
     word = get_word()
     print(f'Слово {i+1}: {morse_encode(word)}')
     answ = input()
     if answ == word:
         print(f'Верно, {word.title()}!')
         answers.append(True)
     else:
         print(f'Неверно, {word.title()}!')
         answers.append(False)

print_statistics(answers)

