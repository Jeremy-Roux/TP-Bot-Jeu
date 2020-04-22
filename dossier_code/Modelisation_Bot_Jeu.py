class Game(object):

    def __init__(self,nb_bat):
        self.nb_bat=nb_bat
        print("Jouez au jeu des batonnets")

    def Rules(self):
        print("Le jeu est composé de 21 batonnets, l'objectif est de ne pas tirer le dernier.")
        print("Chaque joueur doit tirer à tour de rôle, 1, 2 ou 3 batonnets.")

    def is_game_finished(self):
        if self.nb_bat=0:
            return True
        else:
            return False

    def display(self):
        return self.nb_bat*"|"



