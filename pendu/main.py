from affichage import *

from jeu import *

from mots import *

def main():
    while True:
        vies = 6
        mot_secret = choisir_mot()
        lettres_trouvees = ""
        lettre = input("Choisissez une lettre")
        jouer_tour(mot_secret, lettres_trouvees, lettre)
        if lettre in mot_secret: 
            pass
        else:
            vies -= 1
        afficher_pendu(vies)
        if vies == 0:
            print("T'es mort")
            break

main()


