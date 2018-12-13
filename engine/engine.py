from portfolio.python.console_game.classes.mobs import *
from portfolio.python.console_game.funcs.func import *
import sys
# import inspect
from random import randint
current_module = sys.modules[__name__]


arrClass = []
settings.init()

# create mobs
mob1 = Orc()
mob2 = Snake()
mob3 = Snake()
mob4 = Snake()
mob5 = Snake()
mob6 = Snake()
mob7 = Snake()
mob8 = Snake()
mob9 = Horsish()
mob10 = Horsish()
mob11 = Horsish()
mob12 = Horsish()
mob13 = Dead()
mob14 = Dead()
mob15 = Dead()
mob16 = Dead()
mob17 = Dead()
mob18 = Magic()
mob19 = Magic()
mob20 = Magic()
mob21 = Magic()
mob22 = Elf()
mob23 = Elf()
mob24 = Dragon()
mob25 = Dragon()
mob26 = Dragon()

arrClass.append(mob1)
arrClass.append(mob2)
arrClass.append(mob3)
arrClass.append(mob4)
arrClass.append(mob5)
arrClass.append(mob6)
arrClass.append(mob7)
arrClass.append(mob8)
arrClass.append(mob9)
arrClass.append(mob10)
arrClass.append(mob11)
arrClass.append(mob12)
arrClass.append(mob13)
arrClass.append(mob14)
arrClass.append(mob15)
arrClass.append(mob16)
arrClass.append(mob17)
arrClass.append(mob18)
arrClass.append(mob19)
arrClass.append(mob20)
arrClass.append(mob21)
arrClass.append(mob22)
arrClass.append(mob23)
arrClass.append(mob24)
arrClass.append(mob25)
arrClass.append(mob26)

# set mobs skills
for x in arrClass:
    calculate_stats(x)
    set_skills_from_ini(x)


def game(hero):
    while True:
        fight(hero, arrClass[select_enemy(hero)])


def select_enemy(hero):
    print_enemy(hero)
    selected = 0
    while selected == 0:
        selected = int(input('Select enemy: '))
        if selected not in range(1, len(arrClass) + 1):
            print('Wrong enemy!')
            selected = 0
        else:
            selected -= 1
            return selected

    return


def print_enemy(hero):
    # classes = inspect.getmembers(sys.modules[__name__], inspect.isclass)
    # print(classes)

    print('\nYour lev:', hero.Lev, '\n')
    columns = int(len(arrClass) / 3)
    for x in range(columns):
        c1 = '> ' + str(x + 1) + '. ' + str(arrClass[x].Name) + ' - Lev: ' + str(arrClass[x].Lev)
        c2 = '> ' + str(x + 1 * columns + 1) + '. ' + str(arrClass[x + 1 * columns].Name) + \
             ' - Lev: ' + str(arrClass[x + 1 * columns].Lev)
        c3 = '> ' + str(x + 2 * columns + 1) + '. ' + str(arrClass[x + 2 * columns].Name) + \
             ' - Lev: ' + str(arrClass[x + 2 * columns].Lev)
        print('{}{}{}{}{}'.format(c1, (40 - len(c1)) * ' ', c2, (40 - len(c2)) * ' ', c3))

    return


def fight(hero, enemy):
    print('You selected ' + enemy.Name)
    while int(hero.HP) > 0 and int(enemy.HP) > 0:
        print('\nYour turn!')
        selected = select_action()
        print(hero.sound())
        do_action(selected, hero, enemy)

        if int(hero.HP) <= 0 or int(enemy.HP) <= 0:
            break
        else:
            print('\nEnemy turn!')
            print(enemy.sound())
            selected = randint(1, 3)
            do_action(selected, enemy, hero)

    if int(hero.HP) > 0:
        print('You defeat ' + enemy.Name + ', earn ' + str(enemy.Exp) + ' exp!')

        hero.Exp += int(enemy.Exp)
        hero.Win += 1
        add_skill_points(hero, hero.Exp)
    else:
        print('You have been defeated by', enemy.Name)
        hero.Lose += 1

    reset_skills(hero)
    reset_skills(enemy)
    set_skills_to_ini(hero)
    set_skills_from_ini(enemy)

    return


def select_action():
    print('> 1. Attack'
          '\n> 2. Defend'
          '\n> 3. Heal')

    selected = 0
    while selected == 0:
        selected = int(input('Select action: '))
        if selected not in range(1, 4):
            print('Bad action!')
            selected = 0
        else:
            return selected

    return


def do_action(selected, attacker, defender):
    if selected == 1:
        # check critical hit
        rand = randint(0, 100000) / 1000
        boost = attacker.ATK
        critical_damage = False
        if attacker.Chance_critic * 100 > rand:
            boost = attacker.ATK * 3
            critical_damage = True

        if defender.defend:
            damage = boost - round(defender.DEF * 1.2 * 0.3)
        else:
            damage = boost - round(defender.DEF * 0.3)

        if damage < 0:
            damage = 0

        rand = randint(0, 100000) / 1000
        if defender.Dodge * 100 > rand:
            print('\n' + defender.Name + ' dodge!')
        else:
            defender.HP = int(defender.HP) - int(damage)
            if critical_damage:
                print('\n' + attacker.Name + ' CRITICAL HIT ' + defender.Name +
                      ' by ' + str(damage) + ' HP(' + str(defender.HP) + ')')
            else:
                print('\n' + attacker.Name + ' hit ' + defender.Name +
                      ' by ' + str(damage) + ' HP(' + str(defender.HP) + ')')

        if defender.defend:
            defender.defend = False
    elif selected == 2:
        attacker.defend = True
        print('\n' + attacker.Name + ' take shield. Defense was increased!')
    elif selected == 3:
        restore = int(int(attacker.HP) * 0.1)
        attacker.HP = int(attacker.HP) + restore
        print('\n' + attacker.Name + ' healed himself, ' + str(restore) + 'HP have been restored(' +
              str(attacker.HP) + ')')

    return


def add_skill_points(cls, exp):
    skill_points = (round(exp / 100) - int(cls.Lev)) * 2
    if skill_points % 2 != 0:
        skill_points -= 1

    if skill_points > 0:
        print('You earned', skill_points, 'skill points!')
        allocate_skill_points(cls, True, skill_points)

    return
