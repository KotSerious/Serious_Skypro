# Создаем счетчик для ответов, кол-во баллов за ответ, финальный подсчет баллов
counter = 0
scores = 10
user_final_score = 0

# Приветствуем пользователя
print("Привет!", "Предлагаю проверить свои знания английского!", sep="\n")

# Просим пользователя ввести свое имя
user_name = input("Напиши, как тебя зовут. ")

# Приветствуем и начинаем
print(f"Привет, {user_name}, начинаем тренировку!")

# Правильный ответ на вопрос
question_1 = "is"

# Задаем вопрос
answer_1 = input("My name ___ Vova ")

# Проверяем ответ
if (question_1 == answer_1):
    counter += 1
    print("Ответ верный!", f"Вы получаетет {scores} баллов!", sep="\n")
else:
    print("Неправильно.", f"Правильный ответ: {question_1}", sep="\n")

question_2 = "am"

answer_2 = input("I ___ a coder ")

if (question_2 == answer_2):
    counter += 1
    print("Ответ верный!", f"Вы получаетет {scores} баллов!", sep="\n")
else:
    print("Неправильно.", f"Правильный ответ: {question_2}", sep="\n")

question_3 = "in"

answer_3 = input("I live ___ Moscow ")

if (question_3 == answer_3):
    counter += 1
    print("Ответ верный!", f"Вы получаетет {scores} баллов!", sep="\n")
else:
    print("Неправильно.", f"Правильный ответ: {question_3}", sep="\n")

print(f"Вот и все, {user_name}!", f"Вы ответили на {counter} вопросов из 3 верно.", sep=("\n"))

# Умножаем кол-во баллов на ответов
user_final_score = scores * counter
print(f"Вы заработали {user_final_score} баллов.")

# Считаем процент правильных ответов
precent = round(counter * 100 / 3, 2)
print(f"Это {precent} процентов.")
