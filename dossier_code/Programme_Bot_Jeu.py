n = 21
i=int(input("Combien voulez-vous tirer de bâtonnets ?"))
    while i < 1 or i > 3 :
        i = int(input("Veuillez saisir un entier compris entre 1 et 3"))
print("Vous venez de tirer :", i, "batonnets")

n = n - i
    print("Nombre de bâtonnets restants : ", n)