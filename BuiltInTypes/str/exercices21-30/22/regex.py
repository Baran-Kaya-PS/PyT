# Vérifie si une chaîne est un identifiant Python valide.
# contains a-z ; A-Z; 0-9 ; _
# we will use regex
import re

user_input = input("--> ")

if re.fullmatch("^[a-zA-Z_][a-zA-Z_0-9]*$",user_input) is None:
    print(False)
else:
    print(True)