import requests
import random
from BasicWord import BasicWord
from Player import Player


def load_random_word() -> BasicWord:
    """
    Функция возвращает экземпляр класса BasicWord
    """
    data = requests.get("https://www.jsonkeeper.com/b/QI3U").json()
    random_word = random.choice(data)

    return BasicWord(random_word['word'], random_word['subwords'])


def player_registration() -> Player:
    """
    Функция регистрации нового игрока
    """
    player_name = input("Введите имя игрока: ")
    print(f"Привет, {player_name}!")

    return Player(player_name)


def print_statistic(user: Player) -> None:
    """
    Вывод статистики в консоль
    """
    result_line = f"Игра завершена, вы угадали {user.get_used_word_count()}"
    counter = user.get_used_word_count()

    if counter == 0:
        print("Игра завершена, вы не угадали ни одного слова")
    elif counter == 1:
        print(result_line + " слово")
    elif counter in (2, 3, 4):
        print(result_line + " слова")
    elif counter in range(5, 21):
        print(result_line + " слов")
    else:
        print(result_line)
