# Demande une phrase et remplace les espaces multiples par un seul.

user_input = input("--> ")

words = user_input.split()

processed_input = ""
for word in words:
    processed_input+=(word+" ")

print(processed_input)