def new_list():
    nl = []
    print("Veuillez saisir plusieurs nombres")
    for i in range(3):
        user_input = input("-->")
        nl.append(user_input)
    return nl

ntupple = tuple(new_list())
print(ntupple)
ntupple[1] = ntupple[2] # error