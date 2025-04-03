def new_list():
    nl = []
    print("Veuillez saisir plusieurs nombres")
    for i in range(5):
        user_input = input("-->")
        nl.append(user_input)
    user_input = input("-->")
    nl.insert(0, user_input)
    nl.pop()
    return nl

print(new_list())