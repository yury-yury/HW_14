ans_data, right_ans = [('My name ___ Vova', 'is'), ('I ___ a coder', 'am'), ('I live ___ Moscow', 'in')], 0

print('Привет! Предлагаю проверить свои знания английского!')
name = input('Расскажи, как тебя зовут! ')
print(f'Привет, {name}, начинаем тренировку!')

for i in range(len(ans_data)):              # Запускаю цикл с количеством итераций равным числу вопросов
    print(ans_data[i][0])
    ans = input()
    if ans == ans_data[i][1]:               # Если ответ верный, вывожу сообщение
        right_ans += 1
        print('Ответ верный!')
        print('Вы получаете 10 баллов!')
    else:                                   # # Если ответ неверный, вывожу сообщение
        print('Неправильно.')
        print(f'Правильный ответ: {ans_data[i][1]}')

print(f'Вот и все, {name}!')
print(f'Вы ответили на {right_ans} вопросов из 3 верно.')
print(f'Вы заработали {right_ans * 10} баллов.')
print(f'Это {round(right_ans / len(ans_data) * 100)} процентов.')
