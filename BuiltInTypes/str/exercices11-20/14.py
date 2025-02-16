# Découpe une phrase en mots et affiche chaque mot sur une nouvelle ligne

user_input = input("--> ")

words = user_input.split()

for word in words:
    print(word)