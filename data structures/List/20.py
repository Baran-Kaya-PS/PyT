l = "Bonjour à tous".split()
str = ""
while str != "stop":
    print("Tapez un mot de la liste")
    print(l)
    str = input(" -->")
    if str not in l:
        print("Le mot n'est pas dans la liste")
    if str in l:
        print(l.index(str)+1)