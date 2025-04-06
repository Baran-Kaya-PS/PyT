dict = {}
ui = ""
for x in range(5):
    ui = input("Clé : Valeur : ").split()
    dict[ui[0]] = ui[1]

print("Le dictionnaire est")
print(dict)

ui = ""
while ui != "stop":
    print("Demandez quelques clés pour récupérer les valeurs")
    ui = input("Clé, Valeur : ").split()
    if ui[0] in dict:
        print(dict[ui[0]])
    else: dict[ui[0]] = ui[1]