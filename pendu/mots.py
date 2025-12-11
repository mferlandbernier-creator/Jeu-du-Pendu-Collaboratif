import random

def choisir_mot():
    '''
    Fonction qui retourne une de ces mots au hasard:
    python, programmation, github,collaboration
    '''
    mots = ["python", "programmation", "github", "collaboration"]
    return random.choice(mots)