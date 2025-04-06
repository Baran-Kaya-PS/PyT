l = []

for x in range(5):
    ui = input("-->")
    l.append(ui)

l = set(l)
ui = ""
while ui != "stop":
    ui = input("Tapez un mot pour voir si il est contenu dans l'ensemble ")
    if ui in l:
        print("votre mot est bien dans la liste ")
        print(l)