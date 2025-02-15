# Demande une phrase et un mot, puis affiche la position du mot dans la phrase.

find = False
user_input = input("écrivez votre phrase ")

user_word = input("choisis ton mot ")

words = user_input.split()

for index,word in enumerate(words):
    if word == user_word:
        print("Mot trouvé à la "+str(index+1) + "e position")
        find = True
if not find :
    print("Mot pas trouvé")