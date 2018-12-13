from portfolio.python.console_game.classes.player import *
from portfolio.python.console_game.engine.engine import *
import portfolio.python.console_game.settings as settings


if __name__ == "__main__":
    settings.init()
    welcome_screen()

    hero = Player()

    select_option = 0
    while select_option != 5:
        print_menu()
        select_option = int(input('\n\nSelect > '))
        if select_option not in range(0, 6):
            print('\nWrong command!')
            select_option = 0
        else:
            if select_option == 1:
                new_game(hero)
                game(hero)
                select_option = 0
            elif select_option == 2:
                load_game(hero)
                game(hero)
                select_option = 0
            elif select_option == 3:
                print_help()
                select_option = 0
            elif select_option == 4:
                print_stats(hero)
                select_option = 0

    print('Quit...')
