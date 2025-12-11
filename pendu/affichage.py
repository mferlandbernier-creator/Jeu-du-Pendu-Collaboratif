# affichage.py
# Auteur : Jeremy-James (Membre 2)
# Module responsable de l'affichage ASCII du pendu

def afficher_pendu(erreurs):
    """
    Affiche le dessin du pendu selon le nombre d'erreurs (0 à 6).
    """

    stades = [
        """
  +---+
  |   |
      |
      |
      |
      |
=========
""",
        """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
        """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
        """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
        """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
""",
        """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
""",
        """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
"""
    ]

    # Sécuriser erreurs dans la plage 0..6
    erreurs = max(0, min(erreurs, len(stades) - 1))

    print(stades[erreurs])


# Test local
if __name__ == "__main__":
    for i in range(7):
        print(f"Erreurs : {i}")
        afficher_pendu(i)
        input("Entrée pour continuer...")
