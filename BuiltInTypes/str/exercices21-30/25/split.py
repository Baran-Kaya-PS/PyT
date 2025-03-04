import re

phrases = [
    "Le chat dort.",
    "Python est un langage de programmation puissant.",
    "Les montagnes enneigées brillent sous le clair de lune.",
    "L'hippopotomonstrosesquippedaliophobie est la peur des longs mots.",
    "Un éléphant dans un magasin de porcelaine fait des ravages.",
    "Le vent souffle fort dans la vallée encaissée.",
    "Anticonstitutionnellement est l'un des mots les plus longs de la langue française.",
    "J'adore résoudre des problèmes d'algorithmique et d'optimisation."
]

def longest_word(sentence):
    length = 0
    longestword = ""
    words = re.findall(r"\b\w+\b",sentence) # retourne une liste sans ponctuation
    for word in words:
        if length < len(word):
            longestword = word
            length = len(word)
    return (longestword,length)

for sentences in phrases:
    print(longest_word(sentences))