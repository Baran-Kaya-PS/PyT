# Demande une phrase et un mot, puis vérifie si la phrase se termine par ce mot.

print("Ecrivez une phrase")
user_input1 = input("--> ")
print("Ecrivez le mot par lequel la phrase se termine")
user_input2 = input("--> ")

if (user_input1.endswith(user_input2)):
    print("La phrase",user_input1,"fini avec",user_input2)
else:
    print("La phrase",user_input1,"ne fini pas avec",user_input2)