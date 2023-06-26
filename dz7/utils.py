import json
import os


def load_students():
    with open(os.path.join('data', 'students.json'), 'r', encoding='utf8') as file:
        data = json.load(file)
        return data


def load_professions():
    with open(os.path.join('data', 'professions.json'), 'r', encoding='utf8') as file:
        data = json.load(file)
        return data


def get_student_by_pk(pk):
    student_data = load_students()
    for student in student_data:
        if student['pk'] == pk:
            return student


def get_professions_by_title(title):
    professions_data = load_professions()
    for profession in professions_data:
        if profession['title'] == title:
            return profession


def check_fitness(student, profession):
    student_skills = set(student['skills'])
    profession_skills = set(profession['skills'])

    student_has = student_skills.intersection(profession_skills)
    student_lacks = profession_skills.difference(student_skills)

    fitness_percent = len(student_has) / len(profession_skills) * 100

    return {
        'has': list(student_has),
        'lacks': list(student_lacks),
        'fit_recent': int(fitness_percent)
    }


# s1 = get_student_by_pk(1)
# p1 = get_professions_by_title('Backend')
#
# print(check_fitness(s1, p1))
