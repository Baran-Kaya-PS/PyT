def new_list():
    nl = []
    print("Veuillez saisir plusieurs nombres")
    for i in range(3):
        user_input = input("-->")
        nl.append(user_input)
    return nl

nl = new_list()
print(nl)

del(nl[0]) # do not return value
print(nl)