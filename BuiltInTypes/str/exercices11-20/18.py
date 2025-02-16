# Transforme une phrase pour que chaque mot commence par une majuscule.

user_input = input("-->")

processed = ""

for words in user_input.split():
    words = words[0].lower() + words[1:]
    processed+=words + " "
print(processed)