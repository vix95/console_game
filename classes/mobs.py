from random import randint


class Monster:
    __count = 0

    def __init__(self, mob_id='Monster_'):
        self.ID = mob_id + str(Monster.__count)
        self.Name = ''
        self.VIT = 1
        self.ATK = 1
        self.DEF = 0
        self.AGI = 0
        self.HP = 0
        self.Dodge = 0
        self.Chance_critic = 0
        self.Exp = 0
        self.Lev = 1
        self.defend = False
        Monster.__count += 1

    def __del__(self):
        return


class Orc(Monster):
    __count = 0

    def __init__(self, mob_id='Orc_'):
        Monster.__init__(self)
        self.ID = mob_id + str(Orc.__count)
        Orc.__count += 1
        return

    @staticmethod
    def sound():
        selected = randint(0, 2)
        if selected == 0:
            return 'Aaargghhh!'
        elif selected == 1:
            return 'Aaaaaaaaaaarrrrrghhhh!!'
        elif selected == 2:
            return 'Ouuuughhh'

        return

    def __del__(self):
        return


class Snake(Monster):
    __count = 0

    def __init__(self, mob_id='Snake_'):
        Monster.__init__(self)
        self.ID = mob_id + str(Snake.__count)
        Snake.__count += 1
        return

    @staticmethod
    def sound():
        selected = randint(0, 2)
        if selected == 0:
            return 'Ssssss!'
        elif selected == 1:
            return 'Sssshhhh'
        elif selected == 2:
            return 'Sssssssssssss...'

        return

    def __del__(self):
        return


class Horsish(Monster):
    __count = 0

    def __init__(self, mob_id='Horsish_'):
        Monster.__init__(self)
        self.ID = mob_id + str(Horsish.__count)
        Horsish.__count += 1
        return

    @staticmethod
    def sound():
        selected = randint(0, 2)
        if selected == 0:
            return 'Boooo!'
        elif selected == 1:
            return 'Wwwwhhhhhh...'
        elif selected == 2:
            return 'Sssshhhhhhhh...'

        return

    def __del__(self):
        return


class Dead(Monster):
    __count = 0

    def __init__(self, mob_id='Dead_'):
        Monster.__init__(self)
        self.ID = mob_id + str(Dead.__count)
        Dead.__count += 1
        return

    @staticmethod
    def sound():
        selected = randint(0, 2)
        if selected == 0:
            return 'Aaarghhh'
        elif selected == 1:
            return 'Brrhhh!'
        elif selected == 2:
            return 'Braaaaain!'

        return

    def __del__(self):
        return


class Magic(Monster):
    __count = 0

    def __init__(self, mob_id='Magic_'):
        Monster.__init__(self)
        self.ID = mob_id + str(Magic.__count)
        Magic.__count += 1
        return

    @staticmethod
    def sound():
        selected = randint(0, 2)
        if selected == 0:
            return 'Swwwww...'
        elif selected == 1:
            return 'Ssshhhhhhh...'
        elif selected == 2:
            return 'Mmmhhhh...'

        return

    def __del__(self):
        return


class Elf(Monster):
    __count = 0

    def __init__(self, mob_id='Elf_'):
        Monster.__init__(self)
        self.ID = mob_id + str(Elf.__count)
        Elf.__count += 1
        return

    @staticmethod
    def sound():
        selected = randint(0, 2)
        if selected == 0:
            return 'Humans are stupid!'
        elif selected == 1:
            return 'Attaaaaaaaack!!'
        elif selected == 2:
            return 'Love nature!'

        return

    def __del__(self):
        return


class Dragon(Monster):
    __count = 0

    def __init__(self, mob_id='Dragon_'):
        Monster.__init__(self)
        self.ID = mob_id + str(Dragon.__count)
        Dragon.__count += 1
        return

    @staticmethod
    def sound():
        selected = randint(0, 2)
        if selected == 0:
            return 'Zzziiuuuu'
        elif selected == 1:
            return 'Ffffllllhhhhhh...'
        elif selected == 2:
            return 'Ghhhraaaar!!'

        return

    def __del__(self):
        return
