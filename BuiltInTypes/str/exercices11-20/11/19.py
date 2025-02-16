# Remplace les caractères spéciaux , . ; ! ? dans une phrase par des espaces.

to_replace = [",",".",";","!","?"]

user_input = input("-->")

for ch in to_replace:
    user_input = user_input.replace(ch," ")

print(" ".join(user_input.split()))