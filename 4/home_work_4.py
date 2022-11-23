words_easy = {"family":"семья", "hand": "рука", "people":"люди", "evening": "вечер", "minute":"минута"}
words_medium = {"believe":"верить", "feel": "чувствовать", "make":"делать", "open": "открывать", "think":"думать"}
words_hard = {"rural":"деревенский", "fortune": "удача", "exercise":"упражнение", "suggest": "предлагать","except":"кроме"}
levels = {0: "Нулевой", 1: "Так себе", 2: "Можно лучше", 3: "Норм", 4: "Хорошо", 5: "Отлично"}
answers = {}
cnt = 0

print('Выберите уровень сложности.')
print('Легкий, средний, сложный.')
lev = input()
if lev == 'легкий':
    words = words_easy
elif lev == 'средний':
    words = words_medium
else:
    words = words_hard

print('Выбран уровень сложности, мы предложим 5 слов, подберите перевод.')
input('Нажмите Enter')

for key, value in words.items():
    print(f'{key}, {len(value)} букв, начинается на {value[0]}...')
    ans = input()
    if ans == value:
        key = key.title()
        print(f'Верно, {key} — это {value}.')
        answers[key] = True
    else:
        key = key.title()
        print(f'Неверно, {key} — это {value}.')
        answers[key] = False

print()
print('Правильно отвечены слова:')
for key, value in answers.items():
    if value:
        key = key.title()
        print(key)
        cnt += 1
print()
print('Неправильно отвечены слова:')
for key, value in answers.items():
    if not value:
        key = key.title()
        print(key)

print('Программа:Ваш ранг:')
print(levels[cnt])


