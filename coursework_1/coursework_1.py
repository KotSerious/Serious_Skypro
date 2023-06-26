import random

WORDS = [
    'code', 'python', 'programmer',
    'windows', 'linux', 'ubuntu', 'macos',
    'android', 'iphone', 'cat', 'dog',
    'red', 'green', 'blue', 'youtube',
    'twitch', 'trovo', 'stream', 'steam'
]


def get_word():
    """Получает случайное слово
        из списка слов """
    random.shuffle(WORDS)
    return WORDS.pop()


def morse_encode(word: str):
    """
    Шифрует слово в кодморзе
    """
    alphabet = {
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--..",
        ".": ".-.-.-",
        ",": "--..--",
        "?": "..--..",
        "!": "-.-.--",
        "-": "-....-",
        "/": "-..-.",
        "@": ".--.-.",
        "(": "-.--.",
        ")": "-.--.-"
    }
    word_to_lower = list(word.lower())
    keys = list(alphabet.keys())
    coded_word = []
    for el in word_to_lower:
        if el in keys:
            coded_word.append(alphabet[el])
        else:
            print('В слове содержатся не поддерживаемые символы')
            return

    return ' '.join(coded_word)


def print_statistics(answers: list[bool]):
    """"
    Выводит статистику
    """
    print(f'\nВсего задачек: {len(answers)}')
    print(f'Отвечено верно: {answers.count(True)}')
    print(f'Отвечено неверно: {answers.count(False)}')


def main():
    """
    Старт программы
    """
    input('Сегодня мы потренируемся расшифровывать азбуку Морзе \nНажмите Enter и начнем!')
    counter = 1
    ANSWERS = []
    while len(ANSWERS) < 5:
        word = get_word()
        code_word = morse_encode(word)
        # print(word)
        answer = input(f'\nСлово {counter} - {code_word} ')
        if answer == word:
            print(f'Верно, {word}!')
            ANSWERS.append(True)
        else:
            print(f'Неверно, {word}!')
            ANSWERS.append(False)
        counter += 1

    print_statistics(ANSWERS)


main()
