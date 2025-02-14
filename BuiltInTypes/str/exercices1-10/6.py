# Demande une phrase et remplace un mot donné par un autre.
print("Ecrivez une phrase")

user_input1 = input("--> ")

print("Quel mot voulez vous remplacer ?\n",user_input1,"\n")

user_input2 = input("--> ")
print("Par quoi voulez vous le remplacer")
user_input3 = input("--> ")
user_input1 = user_input1.replace(user_input2,user_input3)

print(user_input1)