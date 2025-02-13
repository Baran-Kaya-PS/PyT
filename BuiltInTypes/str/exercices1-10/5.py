# Demande une phrase et une lettre, puis affiche combien de fois la lettre apparaît.
#📌 Pré-requis : Variables, affichage (print()),
# entrée utilisateur (input()), bases des chaînes (.lower(), .upper(), .capitalize(), etc.).

print("Ecrivez une phrase")

user_input1 = input("--> ")

print("Choisissez une lettre pour connaitre sa fréquence dans la phrase")

user_input2 = input("--> ")

print(user_input1.lower().count(user_input2[0].lower()))