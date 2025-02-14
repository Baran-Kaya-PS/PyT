# Demande une phrase et enlève les espaces inutiles au début et à la fin.

print("Ecrivez une phrase")
user_input = input("--> ")

print(user_input.strip()) # or .lstrip().rstrip()