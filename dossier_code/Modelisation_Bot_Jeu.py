class Game(object):

    def __int__(self):
        print("Jouez au jeu des batonnets")

    def Rules(self):
        print("Le jeu est composé de 21 batonnets, l'objectif est de ne pas tirer le dernier.")
        print("Chaque joueur doit tirer à tour de rôle, 1, 2 ou 3 batonnets.")

n=21
i=int(input("Combien voulez-vous tirer de bâtonnets ?")
if i <1:
    print("veuillez saisir un entier compris entre 1 et 3 ")
if i >3:
    print ("veuillez saisir un entier compris entre 1 et 3")
else:
    print("vous avez bien tiré", i)
n=n-i
print("Nombre de bâtonnets restants : ", n)
if n%4==3:
    p=2
elif n%4==2
    p=1
elif n%4==0
    p=3
else:
    p=1
print ("je tire :"p)


