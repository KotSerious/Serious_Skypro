import json
import os


class Question:
    def __init__(self, text, difficulty, answer):
        self.text = text
        self.difficulty = difficulty
        self.answer = answer

        self.is_asked = False
        self.user_answer = None
        self.score = self.difficulty * 10

    def get_points(self):
        """Возвращает int, количество баллов.
        Баллы зависят от **сложности**: за 1 дается **10 баллов**, за 5 дается **50 баллов**.
        """
        return self.score

    def is_correct(self):
        """Возвращает True, если ответ пользователя совпадает 
        с верным ответов иначе False.
        """
        return self.answer == self.user_answer

    def build_question(self):
        """Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5
        """
        return f"Вопрос: {self.text} \nСложность: {self.difficulty}/5"

    def feedback(self):
        """**Возвращает :
        Ответ верный, получено __ баллов
        или
        **Возвращает :
        Ответ неверный, верный ответ __
        """
        if self.is_correct():
            return f"Ответ верный, получено {self.score}"
        else:
            return f"Ответ неверный, верный ответ {self.answer}"


def load_question(filename):
    with open(os.path.join('data', 'Question.json'), 'r', encoding='utf8') as file:
        data = json.load(file)

    questions = []
    for quest in data:
        text = quest["q"]
        difficulty = int(quest["d"])
        answer = quest["a"]
        question = Question(text, difficulty, answer)
        questions.append(question)

    return questions


def statistic(questions):
    score = 0
    count = 0

    for question in questions:
        if question.is_correct():
            score += question.score
            count += 1

    return f"Вот и всё! \n"\
           f"Отвечено {count} вопроса из {len(questions)} \n" \
           f"Набрано баллов: {score}"
