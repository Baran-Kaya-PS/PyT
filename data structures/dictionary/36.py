# 36. **Looping Through Dictionaries**
#     Create a dictionary (e.g. `product > price`).
#     Loop over it with `items()` to print each key/value pair.
#     Then print only the keys (`keys()`) and only the values (`values()`).

l2 = "Kebab Panini Hamburger Frites Boisson".split()
l1 = [5,3.55,3.5,1.5,1] # les clés doivent être uniques

l3 = dict(zip(l1,l2))

for pair in l3.items():
    # print(pair) # key/value
    print(pair[0]) #key