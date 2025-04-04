def new_list():
    nl = []
    for i in range(5):
        user_input = input()
        nl.append(user_input)
    print(nl)
    return nl

nl = new_list()

user_input = input("--> ")
if user_input not in nl:
    nl.append(user_input)
    print(user_input+ " à été ajouté à la liste : ")
    print(nl)
else :
    print("la valeur est dans la liste")