def new_list():
    nl = []
    for i in range(5):
        user_input = input()
        nl.append(user_input)
        nl.append(user_input)
    nl.remove(nl[0])
    print(nl)
    nl.clear()
    return nl

print(new_list())