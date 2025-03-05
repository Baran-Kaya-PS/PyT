import re
from functools import reduce

pattern = r"[\w]+"

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
    words = re.findall(pattern,sentence)
    maxlenword = reduce(lambda x,y: x if len(x) > len(y) else y,words)
    return (maxlenword,len(maxlenword))

for sentences in phrases:
    print(longest_word(sentences))
