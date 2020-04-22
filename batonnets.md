# Le jeu des bâtonnets

Critères de notation:

* Difficulté du sujet choisi 
* Lisibilité du code
* Effort de groupe, au moins 1 commit par membre du groupe (pas de commit = pas de note!)

## Enoncé du problème

Le jeu des bâtonnets est un classique de Fort Boyard parmi les duels dans la salle des Maîtres du Temps. Ce jeu se joue à deux (Maître du temps contre un candidat). 
Plusieurs bâtonnets blancs sont disposés devant eux et chacun son tour, les joueurs enlèvent 1, 2 ou 3 bâtons. 
Le joueur qui prend le dernier bâtonnet sur le plateau perd la partie. 

C’est le candidat qui débute la partie.

![Exemple](https://i.ytimg.com/vi/tng717lJlnA/hqdefault.jpg)

Le but de l'exercice est d'implémenter un bot qui jouera contre un joueur humain.

## Modélisation

On modélisera le jeu à l'aide d'une unique classe `Game`.

La classe `Game` est constituée d'un unique attribut:

* un entier qui représente le nombre de bâtonnets présent sur le plateau. 

La classe `Game` contient plusieurs méthodes :

* `is_game_finished` qui renvoie True si la partie est finie

* `display` qui affiche à l'écran le nombre de bâtonnets restants en utilisant une répétition de symbole `|` (option + maj + L sous macOs)

* `player_remove_stick` qui demande à l'utilisateur de choisir un nombre entre 1 et 3 et enlève le nombre de bâtonnets équivalents. 

* `bot_remove_stick` qui enlève aléatoirement entre 1 et 3 bâtonnets.

## Implémentation

### Première implémentation

Le premier objectif est d'implémenter un programme qui permet de lancer une nouvelle partie. 

* Initialisation d'un nouveau jeu. On décide que le jeu commence avec 21 bâtonnets.

* Tant que le jeu n'est pas fini :

	* Retirer le nombre de bâtonnets choisi par le joueur
	
	* Si le jeu est fini :
		* Afficher le message : "L'ordinateur a gagné !"
		
	* Sinon :
	
		* Retirer le nombre de bâtonnets choisi par le bot
		
		* Si le jeu est fini : 
		
			* Afficher le message : "Vous avez gagné !"
			
Pensez à soigner l’interaction avec le joueur pour que l'écran soit lisible et compréhensible.

### Amélioration de la stratégie du bot

Dans un second temps, nous voulons améliorer la stratégie du bot pour la rendre plus optimale. 

On va donc modifier la méthode `bot_remove_stick`.

Essayer d'implémenter la stratégie expliquée dans [cette vidéo](https://www.youtube.com/watch?v=l68oiOnTqFE).

## Tests unitaires

Ecrire des tests unitaires vérifiant le bon fonctionnement des méthodes implémentées.
