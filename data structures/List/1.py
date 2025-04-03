def new_list():
    values = []
    for i in range(5):
        user_input = input("-->")
        values.append(user_input)
    return values

val = new_list()

print(val)
