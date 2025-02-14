# Demande une phrase et un mot, puis vérifie si la phrase commence par ce mot.

print("Ecrivez une phrase")
user_input1 = input("--> ")
print("Ecrivez le mot par lequel la phrase commence")
user_input2 = input("--> ")

if (user_input1.startswith(user_input2)):
    print("La phrase",user_input1,"commence avec",user_input2)
else:
    print("La phrase",user_input1,"ne commence pas avec",user_input2)