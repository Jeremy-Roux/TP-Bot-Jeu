
from Modelisation_Bot_Jeu import *

jeu=Game(21)

while jeu.is_game_finished() == False :
    print("Voici le plateau : ")
    jeu.display()
    jeu.player_remove_stick()
    if jeu.is_game_finished() == True :
        print("L'ordinateur a gagné !")
    else :
        jeu.bot_remove_stick()
        if jeu.is_game_finished() == True:
            print("Vous avez gagné !")
