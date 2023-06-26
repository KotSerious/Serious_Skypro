from utils import get_student_by_pk, get_professions_by_title, check_fitness


def main():
    student_pk = input('Введите номер студента: ')

    if student_pk.isdigit():
        student = get_student_by_pk(int(student_pk))

        if student:
            print(f'Студент {student["full_name"]}')
            print(f'Знает {", ".join(student["skills"])}')
            profession_title = input(f'Выберите специальность для оценки студента {student["full_name"]}: ').title()
            profession = get_professions_by_title(profession_title)

            if profession:
                fitness = check_fitness(student, profession)
                print(f'Пригодность {fitness["fit_recent"]}%')
                print(f'{student["full_name"]} знает {", ".join(fitness["has"])}')
                print(f'{student["full_name"]} не знает {", ".join(fitness["lacks"])}')
            else:
                print('У нас нет такой специальности')
                return main()
        else:
            print('У нас нет такого студента')
            return main()
    else:
        print('Не верный номер студента!')
        return main()


main()
