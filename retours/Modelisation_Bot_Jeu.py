from random import randint


class Game(object):

    def __init__(self, nb_bat):
        self.nb_bat = nb_bat
        print("Jouez au jeu des batonnets")

    def Rules(self):
        print("Le jeu est composé de 21 batonnets, l'objectif est de ne pas tirer le dernier.")
        print("Chaque joueur doit tirer à tour de rôle, 1, 2 ou 3 batonnets.")

    def is_game_finished(self):
        if self.nb_bat == 0:  # pour vérifier l'égalité on utilise ==
            return True
        else:
            return False

    def player_remove_stick(self):

        # TODO: corriger cette méthode

        # j'ai repris ici le code que vous avez écrit dans Programme_Bot_Jeu

        i = int(input("Combien voulez-vous tirer de bâtonnets ?"))

        while i < 1 or i > 3:
            i = int(input("Veuillez saisir un entier compris entre 1 et 3"))

        print("Vous venez de tirer :", i, "batonnets")

        # j'ai juste ajouté la ligne ci-dessous pour retirer du jeu les i bâtonnets

        self.nb_bat = self.nb_bat - i

    def bot_remove_stick(self):

        i = randint(1, 3)  # par exemple, je tire un nombre au hasard entre 1 et 3

        # TODO: sur le modèle de la méthode player_remove_stick, implémenter cette méthode

        self.nb_bat = self.nb_bat - i  # on retire du jeu les i bâtonnets

    def display(self):
        return self.nb_bat * "|"
