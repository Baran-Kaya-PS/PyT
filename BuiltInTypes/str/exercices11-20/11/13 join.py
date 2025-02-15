# Demande une phrase et remplace les espaces multiples par un seul.

user_input = input("--> ")

words = user_input.split()

processed_input = " ".join(words)

print(processed_input)