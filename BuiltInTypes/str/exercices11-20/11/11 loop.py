# Demande une phrase et affiche-la à l’envers.

user_input = input("--> ")
reverse = ""
for i in reversed(range(0,len(user_input))):
    reverse += user_input[i]

print(reverse)