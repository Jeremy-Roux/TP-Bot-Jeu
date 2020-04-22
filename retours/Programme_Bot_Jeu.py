from retours.Modelisation_Bot_Jeu import Game

"""
Implémentation de la partie:

Le programme est complet:
vous pouvez exécuter le code pour vérifier que vos méthodes fonctionnent correctement

Actuellement, la partie ne s'arrête jamais.
C'est parce qu'il y a un petit soucis dans votre méthode player_remove_stick() ==> je vous laisse trouver lequel

Conseils/Indications: 
Que se passe-t-il lorsqu'il reste 2 bâtonnets et que vous en retirez 3 ?
Lancez le programme et testez ce cas
"""


"""
Initialisation d'un nouveau jeu
"""
jeu = Game(21)  # on crée un nouveau Game avec 21 bâtonnets
jeu.Rules()     # on affiche les règles du jeu

"""
Commencer à jouer 
"""

while not jeu.is_game_finished():  # TantQue le jeu n'est pas fini

    print(jeu.display())        # on affiche le nombre de bâtonnets à l'écran

    jeu.player_remove_stick()   # l'utilisateur retire un bâtonnet du jeu

    if jeu.is_game_finished():  # on vérifie si le jeu est terminé

        print("Vous avez perdu!")  # si oui le joueur perdu

    else:  # si le jeu n'est pas terminé alors c'est au tour du bot de joueur

        jeu.bot_remove_stick()   # le bot retire un bâtonnet du jet

        if jeu.is_game_finished():  # on vérifie si le jeu est terminé

            print("Vous avez gagné!")  # si oui le joueur a gagné

