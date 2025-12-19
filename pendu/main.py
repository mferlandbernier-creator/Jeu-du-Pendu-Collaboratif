from affichage import *

from jeu import *

from mots import *


def main():
    mauvaise_lettre = 0
    mot_secret = choisir_mot()
    print(mot_secret) # utilisé pour les tests
    lettres_trouvees = ["_"] * len(mot_secret)
    while True:
        lettre = input("Choisissez une lettre \n")
        jouer_tour(mot_secret, lettres_trouvees, lettre)
        if not lettre in mot_secret: 
            mauvaise_lettre += 1
        print(lettres_trouvees)
        afficher_pendu(mauvaise_lettre)
        if not "_" in lettres_trouvees:
            print("T'as gagné !")
            break
        if mauvaise_lettre == 6:
            print("T'es mort")
            break

main()


