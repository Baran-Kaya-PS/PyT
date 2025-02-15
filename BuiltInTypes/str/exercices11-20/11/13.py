# Demande une phrase et remplace les espaces multiples par un seul.

user_input = input("--> ")

word_array = user_input.split()

processed_input = ""
for word in word_array:
    processed_input+=(word+" ")

print(processed_input)