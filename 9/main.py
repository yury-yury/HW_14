from players import Player
from basic_word import BasicWord
from functions import suffix_definition


def main():
    """
    The wrapper function ensures consistent execution of all code functions.
    """
    print('Ввведите имя игрока')
    name = input()
    player = Player(name)
    print(f'\nПривет, {name}!')

    game = BasicWord()
    print(f"Составьте {game.count_subword()} слов из слова '{game.word}'")
    print('Слова должны быть не короче 3 букв')
    print('Чтобы закончить игру, угадайте все слова или напишите stop')
    print('Поехали, ваше первое слово?', end='\n')

    while player.count_subword() < game.count_subword():
        word_user = input()

        if word_user == 'stop' or word_user == 'стоп':
            break

        if game.check_word(word_user) and player.check_word(word_user):
            print('верно')
            player.add_word(word_user)

    cnt = player.count_subword()

    print(f'Игра завершена, вы угадали {cnt} слов{suffix_definition(cnt)}!')

if __name__ == '__main__':
    main()