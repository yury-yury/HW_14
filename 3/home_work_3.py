
questions = ["My name ___ Vova", "I ___ a coder", "I live ___ Moscow"]
answers = ["is", "am", "in"]
right_ans, counter_score = 0, 0

print('Привет! Предлагаю проверить свои знания английского! Наберите "ready", чтобы начать!')
if input() == "ready":
    for i in range(len(questions)):
        print(questions[i])
        for j in range(3, 0, -1):
            ans = input()
            if ans == answers[i]:
                right_ans += 1
                counter_score += j
                print('Ответ верный!')
                break
            else:
                if j > 1:
                    print(f'Осталось попыток: {j-1}, попробуйте еще раз!')
                else:
                    print(f'Увы, но нет. Верный ответ: {answers[i]}')

    print(f'Вот и все. Вы ответили на {right_ans} вопросов из {len(questions)} верно. '
          f'Вы набрали {counter_score} баллов..')

else:
    print('Кажется, вы не хотите играть. Очень жаль')
