import random


def loading_words():
    """
     The function receives data from an external file and returns it as a list of strings.
    """
    res = []
    with open('words.txt', 'r', encoding='utf-8') as file:
        for word in file:
            res.append(word.strip())
        return res


def reading_story():
    """
    The function receives data from an external file and returns in the form of a dictionary
    where the names of the players are used as keys, and the maximum result is used as values.
    """
    top_result = {}
    with open('history.txt', 'r', encoding='utf-8') as file:
        for item in file:
            key, value = item.rstrip().split(' ')
            top_result[key] = value

    return top_result


def writing_story(my_dict):
    """
    The function receives data in the form of a dictionary where the names of the players
    are used as keys, and the maximum result is used as values and writes data to an external file.
    """
    with open('history.txt', 'w', encoding='utf-8') as file:
        for item in my_dict.items():
            key, value = item
            file.write(f'{key} {value}\n')



user_res = 0
data = loading_words()

print('Введите ваше имя')
user_name = input()

print(f'Введите количество раундов игры')
n = int(input())

for i in range(n):
    word = data[random.randint(0, len(data))]
    word_list = list(word)
    random.shuffle(word_list)
    mix_word = ''.join(word_list)
    print(f'Угадайте слово - {mix_word}')
    answ = input()
    if answ == word:
        print('Верно! Вы получаете 10 очков.')
        user_res += 10
    else:
        print(f'Неверно! Верный ответ – {word}')

print(f'Ваш результат {user_res} из {n * 10} возможных')

top_story = reading_story()
if user_name in top_story.keys():
    if int(top_story[user_name]) < user_res:
        top_story[user_name] = user_res
else:
    top_story[user_name] = user_res
print(f'Максимальный рекорд: {top_story[user_name]}')

writing_story(top_story)
