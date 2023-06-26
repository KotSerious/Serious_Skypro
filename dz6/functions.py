from random import shuffle


def read_file(filename: str) -> str:
    '''функция чтения файла'''
    with open(filename) as f:
        return f.read()


def write_file(filename: str, content: str) -> None:
    '''функция записи в файл'''
    with open(filename, "a") as f:
        f.write(content)


def get_words() -> list[str]:
    """"получаем слова из файла"""
    content = read_file("words.txt")
    return [el.strip() for el in content.split("\n") if el.strip()]


def shuffle_words(word: str) -> str:
    """"перемешивание слова"""
    tmp = list(word)
    shuffle(tmp)
    return "".join(tmp)


def save_history(name: str, points: int) -> None:
    """"сохраняем историю"""
    content = f"{name}={points}\n"
    write_file("history.txt", content)


def show_stats() -> None:
    """выводим статистику"""
    history = read_file("history.txt").split("\n")
    points = []
    for line in history:
        if line:
            _, point = line.split("=")
            points.append(int(point))

    print(  # noqa: T201
        f"Всего игр сыграно: {len(points)}\n" f"Максимальный рекорд: {max(points)}",
    )
