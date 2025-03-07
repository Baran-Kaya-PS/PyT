test_cases = [
    "Bonjour tout le monde.",  # ✅ 4 mots
    "Python est un langage puissant et flexible.",  # ✅ 7 mots
    "J'adore programmer en Python!",  # ✅ 4 mots (avec apostrophe)
    "  Espaces    multiples    entre   les mots.  ",  # ✅ 5 mots (doit bien gérer les espaces)
    "Les montagnes enneigées brillent sous le clair de lune.",  # ✅ 9 mots
    "C'est l'heure d'apprendre les regex.",  # ✅ 5 mots (doit bien gérer les apostrophes)
    "Un, deux, trois... Action!",  # ✅ 4 mots (doit bien gérer la ponctuation)
    "",  # ✅ 0 mot (cas vide)
    "       ",  # ✅ 0 mot (seulement des espaces)
    "Le vent souffle fort dans la vallée encaissée.",  # ✅ 8 mots
    "Python, C++, et JavaScript sont des langages de programmation.",  # ✅ 9 mots (doit bien gérer les virgules)
    "42 est la réponse à tout.",  # ✅ 6 mots (chiffres inclus)
]

def number_of_words(sentence):
    return len(sentence.split())

for test in test_cases:
    print(number_of_words(test))