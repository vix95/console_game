from random import randint


class Player:
    def __init__(self, player_id='Hero'):
        self.ID = player_id
        self.Name = ''
        self.VIT = 1
        self.ATK = 1
        self.DEF = 0
        self.AGI = 0
        self.HP = 0
        self.Dodge = 0
        self.Chance_critic = 0
        self.Exp = 0
        self.Win = 0
        self.Lose = 0
        self.Lev = 1
        self.defend = False

    @staticmethod
    def sound():
        selected = randint(0, 2)
        if selected == 0:
            return 'Fus Ro Dah!'
        elif selected == 1:
            return 'You will die!'
        elif selected == 2:
            return 'Mmmmm...'

        return

    def __del__(self):
        return
