from random import randint

class Game :

    def __init__(self,nb_bat):
        self.nb_bat=nb_bat

    def is_game_finished(self):
        if self.nb_bat <= 0:
            return True
        else:
            return False

    def display(self):
        print(self.nb_bat*"|")

    def player_remove_stick(self):
        n = int(input("Combien voulez-vous tirer de bâtonnets ? "))
        if self.nb_bat >= 3:
            while n < 1 or n > 3:
                n = int(input("Veuillez saisir un entier compris entre 1 et 3 : "))
        else:
            while n < 1 or n > self.nb_bat:
                n = int(input("Veuillez saisir un entier compris entre 1 et "+str(self.nb_bat)+": "))
        self.nb_bat = self.nb_bat - n

    def bot_remove_stick(self):
        if self.nb_bat >= 3:
            i = randint(1,3)
        else :
            i = randint(1,self.nb_bat)
        self.nb_bat = self.nb_bat - i
        print("Le robot a tiré",i,"bâtonnets")