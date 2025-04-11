# 37. **Sort a Dictionary by Value**
#     Reuse a dictionary (e.g. `name > score`).
#     Convert it to a list of tuples with `items()`.
#     Sort the list of tuples by the score (the value).
#     Rebuild a new dictionary sorted by that criterion.

l2 = "Kebab Panini Hamburger Frites Boisson".split()
l1 = [5,3.55,3.5,1.5,1]

l3 = dict(zip(l1,l2))

l3 = l3.items()

l3 = sorted(l3,key=lambda x : x[0])

l3 = dict(l3)

print(l3)