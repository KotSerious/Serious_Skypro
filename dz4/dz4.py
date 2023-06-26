words_easy = {
    "family":"семья",
    "hand": "рука",
    "people":"люди",
    "evening": "вечер",
    "minute":"минута",
}

words_medium = {
    "believe":"верить",
    "feel": "чувствовать",
    "make":"делать",
    "open": "открывать",
    "think":"думать",
}

words_hard   = {
    "rural":"деревенский",
    "fortune": "удача",
    "exercise":"упражнение",
    "suggest": "предлагать",
    "except":"кроме",
}

levels = {
   0: "Нулевой",
   1: "Так себе",
   2: "Можно лучше",
   3: "Норм",
   4: "Хорошо",
   5: "Отлично",
}

answers = {}
words = {}

#start
response = input("Введите уровень сложности easy/medium/hard: ")

if response.lower() == "easy":
    words = words_easy
elif response.lower() == "medium":
    words = words_medium
elif response.lower() == "hard":
    words = words_hard
else:
    print("Такого уровня сложности нет!")
    quit()

for key, answer  in words.items():
    print(f'{key}, {len(answer)} букв, начинается на {answer[0]}...')
    response_answer = input()
    if response_answer == answer:
        print(f'Верно, {key} - это {answer}')
        answers[key] = True
    else:
        print(f'Неверно, {key} - это {answer}')
        answers[key] = False

#finish
print('Правильно отвеченные слова:')
right_answer = [key for key, answer in answers.items() if answer is True]
print('\n'.join(right_answer))

print('Неправильно отвеченные слова')
failed_answer = [key for key, answer in answers.items() if answer is False]
print('\n'.join(failed_answer))

print(f'Ваш ранг:{levels[len(right_answer)]}')
