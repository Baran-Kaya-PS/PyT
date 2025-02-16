# Demande une phrase et compte combien de voyelles (a, e, i, o, u) elle contient.

user_input = input("--> ").lower()
cpt = 0
voyelles = ["a","e","i","o","u"]

for ch in user_input:
    if ch in voyelles:
        cpt+=1

print("il y a ",cpt," voyelles dans ",user_input)