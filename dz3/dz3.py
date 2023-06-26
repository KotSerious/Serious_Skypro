# Создаем список вопров и ответов
questions = ['My name ___  Vova ', 'I ___ a coder ', 'I live ___ Moscow ']
answers = ['is', 'am', 'in']

# Приветствуем пользователя
print('Привет! Предлагаю проверить свои знания английского!')

# Просим пользователя ввести ready
user_input = input('Наберите "ready", чтобы начать! ')

counter = 0
if user_input == 'ready':
    for i in range(len(questions)):
        answer = input(questions[i])
        if answer == answers[i]:
            print('Ответ верный!')
            counter += 1
        else:
            print(f'Неправильно. Правильный ответ: {answers[i]}')

    percent = round(counter / len(questions) * 100, 2)
    print(f'Вот и всё! Вы ответили на {counter} вопросов из {len(questions)} верно, это {percent} процентов.')

else:
    print('Кажется, вы не хотите играть. Очень жаль.')
