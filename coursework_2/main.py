import utils


def main() -> None:
    player = utils.player_registration()
    random_word = utils.load_random_word()

    print(f'Составьте {random_word.get_sub_word_count()} слов из слова {random_word.word.upper()}')
    print("Слова должны быть не короче 3 букв")
    print('Чтобы закончить игру, угадайте все слова или напишите "stop"')
    print("Поехали, ваше первое слово?")

    while random_word.get_sub_word_count() != player.get_used_word_count():
        user_input = input("Ввод: ").lower().strip()

        if user_input in ("stop", "стоп"):
            utils.print_statistic(player)
            quit()

        if len(user_input) < 3:
            print("Cлишком короткое слово")
            continue

        if random_word.check_sub_word(user_input):
            if player.check_used_word(user_input) is False:
                print("Верно!")
                player.add_used_word(user_input)
            else:
                print("Уже использовано")
        else:
            print("Неверно!")

    utils.print_statistic(player)


main()
