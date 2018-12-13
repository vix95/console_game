import configparser
import portfolio.python.console_game.settings as settings


def welcome_screen():
    print('=' * 40)
    print('=' + ' ' * 38 + '=')
    print('=' + ' ' * 10 + 'Python Console War' + ' ' * 10 + '=')
    print('=' + ' ' * 38 + '=')
    print('=' * 40)
    return


def print_menu():
    print('\n> 1. New Game'
          '\n> 2. Load Game'
          '\n> 3. Help'
          '\n> 4. Stats'
          '\n> 5. Quit')
    return


def print_help():
    print('Python Console War Manual'
          '\n\nYour hero have 4 skills (HP, ATK, DEF, AGI).'
          '\nFor each level up you receive 2 skill points.'
          '\nFor each defeat monster you receive a couple EXP.'
          '\nIf you feel that you will defeat evil you can'
          '\nstart boss fight.'
          '\nBe careful, if you lose then you will lose progress!')
    return


def new_game(hero):
    print_intro_text()
    allocate_skill_points(hero, False, 10)
    set_skills_from_ini(hero)
    print_intro_text2()
    return


def print_intro_text():
    print('Welcome Hero.'
          '\nAn interesting and challenging game awaits you!'
          '\nYou start as a weak warrior. To get to the top you'
          '\nhave to overcome a lot of monsters and gain experience.'
          '\nIf you defeat all mad monsters and EVIL you will be'
          '\nawarded a huge prize!')

    print('First you have to 10 skill points to give away.'
          '\nYou have 4 skills to choose: VIT, STR, DEF, AGI')


def print_intro_text2():
    print('\nYou assigned all available skill points. Your adventure begins!\n')


def allocate_skill_points(hero, lev_up, skill_points):
    config = configparser.ConfigParser()
    config.read(getattr(settings, 'config_file'))

    if not lev_up:
        name = str(input('Type your name: '))
        config.set(hero.ID, 'Name', name)

    while skill_points != 0:
        points = int(input('Enter points you want to assign to VIT (0 - ' + str(skill_points) + '): '))
        correct, skill_points, points = correct_enter_points(points, skill_points)
        if correct:
            config.set(hero.ID, 'VIT', str(points))

        if skill_points == 0:
            break

        points = int(input('Enter points you want to assign to ATK (0 - ' + str(skill_points) + '): '))
        correct, skill_points, points = correct_enter_points(points, skill_points)
        if correct:
            config.set(hero.ID, 'ATK', str(points))

        if skill_points == 0:
            break

        points = int(input('Enter points you want to assign to DEF (0 - ' + str(skill_points) + '): '))
        correct, skill_points, points = correct_enter_points(points, skill_points)
        if correct:
            config.set(hero.ID, 'DEF', str(points))

        if skill_points == 0:
            break

        points = int(input('Enter points you want to assign to AGI (0 - ' + str(skill_points) + '): '))
        correct, skill_points, points = correct_enter_points(points, skill_points)
        if correct:
            config.set(hero.ID, 'AGI', str(points))

        if skill_points == 0:
            break

    # add other stats
    config.set(hero.ID, 'Exp', str(0))
    config.set(hero.ID, 'Lev', str(1))
    config.set(hero.ID, 'Win', str(0))
    config.set(hero.ID, 'Lose', str(0))
    calculate_stats(hero)
    with open(getattr(settings, 'config_file'), 'w') as configfile:
        config.write(configfile)

    return


def correct_enter_points(points, skill_points):
    while int(points) not in range(0, skill_points + 1):
        points = int(input('Enter correct value (0 - ' + str(skill_points) + '): '))

    skill_points -= points
    return True, skill_points, points


def calculate_stats(cls):
    config = configparser.ConfigParser()
    config.read(getattr(settings, 'config_file'))

    config.set(cls.ID, 'HP', str(int(config.get(cls.ID, 'VIT')) * 10 + 10))  # HP
    config.set(cls.ID, 'Dodge', str(round(int(config.get(cls.ID, 'AGI')) * 0.0001, 3)))  # Dodge
    config.set(cls.ID, 'Chance_critic', str(round(int(config.get(cls.ID, 'AGI')) * 0.0003 +
                                                  int(config.get(cls.ID, 'ATK')) * 0.0008, 3)))  # Chance Critic

    if cls.ID == 'Hero':
        config.set(cls.ID, 'Lev', str(int(int(config.get(cls.ID, 'Exp')) / 100 + 1)))  # Lev

    with open(getattr(settings, 'config_file'), 'w') as configfile:
        config.write(configfile)

    return


def load_game(hero):
    set_skills_from_ini(hero)
    calculate_stats(hero)
    set_skills_to_ini(hero)
    set_skills_from_ini(hero)
    return


def set_skills_from_ini(cls):
    config = configparser.ConfigParser()
    config.read(getattr(settings, 'config_file'))

    cls.Name = str(config.get(cls.ID, 'name'))
    cls.VIT = int(config.get(cls.ID, 'vit'))
    cls.ATK = int(config.get(cls.ID, 'atk'))
    cls.DEF = int(config.get(cls.ID, 'def'))
    cls.AGI = int(config.get(cls.ID, 'agi'))
    cls.HP = int(config.get(cls.ID, 'hp'))
    cls.Dodge = float(config.get(cls.ID, 'dodge'))
    cls.Chance_critic = float(config.get(cls.ID, 'chance_critic'))
    cls.Exp = int(config.get(cls.ID, 'exp'))
    cls.Lev = int(config.get(cls.ID, 'lev'))

    if cls.ID == 'Hero':
        cls.Win = int(config.get(cls.ID, 'win'))
        cls.Lose = int(config.get(cls.ID, 'lose'))

    return


def print_stats(hero):
    set_skills_from_ini(hero)
    calculate_stats(hero)
    print('\n\nWelcome ' + hero.Name + ' it\'s your stats:')
    print('{}: {}{}{}: {}'.format('VIT', hero.VIT, (20 - len(str(hero.VIT))) * ' ', 'HP', hero.HP))
    print('{}: {}{}{}: {:.1f}%'.format('ATK', hero.ATK, (20 - len(str(hero.ATK))) * ' ',
                                       'Dodge', float(hero.Dodge * 100)))
    print('{}: {}{}{}: {:.1f}%'.format('DEF', hero.DEF, (20 - len(str(hero.DEF))) * ' ',
                                       'Chance critic', float(hero.Chance_critic * 100)))
    print('{}: {}'.format('AGI', hero.AGI))
    print('\n{}: {}{}{}: {}'.format('Exp', hero.Exp, (20 - len(str(hero.Exp))) * ' ',
                                    'Win', hero.Win))
    print('{}: {}{}{}: {}'.format('Lev', hero.Lev, (20 - len(str(hero.Lev))) * ' ',
                                  'Lose', hero.Lose))
    return


def reset_skills(cls):
    config = configparser.ConfigParser()
    config.read(getattr(settings, 'config_file'))
    cls.HP = str(config.get(cls.ID, 'HP'))
    cls.defend = False
    return


def set_skills_to_ini(cls):
    config = configparser.ConfigParser()
    config.read(getattr(settings, 'config_file'))
    config.set(cls.ID, 'VIT', str(cls.VIT))  # VIT
    config.set(cls.ID, 'ATK', str(cls.ATK))  # ATK
    config.set(cls.ID, 'DEF', str(cls.DEF))  # DEF
    config.set(cls.ID, 'AGI', str(cls.AGI))  # AGI
    config.set(cls.ID, 'Exp', str(cls.Exp))  # Exp
    config.set(cls.ID, 'Win', str(cls.Win))  # Win
    config.set(cls.ID, 'Lose', str(cls.Lose))  # Lose

    with open(getattr(settings, 'config_file'), 'w') as configfile:
        config.write(configfile)

    calculate_stats(cls)
    return
