questions = ["My name ___ Vova", "I ___ a coder", "I live ___ Moscow"]
answers = ["is", "am", "in"]
def greteeng():
    """Функция приветствие"""
    print('Привет! Предлагаю проверить свои знания английского! Наберите "ready", чтобы начать!')
    if input() == "ready":
        return True
    return False

def game():
    right_ans, counter_score = 0, 0
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
    return (right_ans, counter_score)

def display(right_ans, counter_score):
    print(f'Вот и все. Вы ответили на {right_ans} вопросов из {len(questions)} верно. '
          f'Вы набрали {counter_score} баллов..')

def main():
    if not greteeng():
        print('Кажется, вы не хотите играть. Очень жаль')
        return
    right_ans, counter_score = game()
    display(right_ans, counter_score)


# main()
print(greteeng())