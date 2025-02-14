# Demande une phrase et affiche-la à l’envers.

print("Ecrivez une phrase")

user_input = input("--> ")

# slicing s[start:end:step]; by default start end are 0,n & step can be negative

print(user_input[::-1])