# Demande un mot et affiche si celui-ci est entièrement en majuscule ou non.
#📌 Pré-requis : Variables, affichage (print()),
# entrée utilisateur (input()), bases des chaînes (.lower(), .upper(), .capitalize(), etc.).

print("Ecrivez une phrase")

user_input = input("--> ")

if user_input.isupper():
    print("La phrase est en majuscule")
elif user_input.islower():
    print("La phrase est en minuscule")
else:
    print("La phrase est en minuscule et en majuscule")