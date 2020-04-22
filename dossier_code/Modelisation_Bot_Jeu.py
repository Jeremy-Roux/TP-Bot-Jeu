from random import randint
class Game :

    def__init__(self,nb_bat):
    self.nb_bat=nb_bat

    def is_game_finished(self):
        if self.nb_bat <=0:
            return True
        else:
            return False

