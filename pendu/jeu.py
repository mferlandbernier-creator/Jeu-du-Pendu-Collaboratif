
def jouer_tour (mot_secret, lettres_trouvees, lettre):
    lettre = lettre.lower()

    if lettre in mot_secret:
        for position, lettre_mot in enumerate(mot_secret):
            if lettre_mot == lettre:
                lettres_trouvees[position] = lettre
        trouve = True
    else:
        trouve = False

    return lettres_trouvees, trouve