import random

from homework.dz8.utils import load_question, statistic
from fileinput import filename

if __name__ == "__main__":
    questions = load_question(filename)

    random.shuffle(questions)

    for question in questions:
        print(question.build_question())
        user_answer = input("Ответ: ")
        question.user_answer = user_answer
        print(question.feedback())

    print(statistic(questions))
