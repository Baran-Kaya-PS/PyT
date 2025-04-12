# 41. **Create a Small Inventory (Dictionary)**
#     Request multiple pairs `(item_name, quantity)` from the user.
#     Store them in a dictionary, adding up the quantities if the item name already exists.
#     Print the final dictionary.
from random import randint

item_name = "Eau Lait Beurre Semoule Riz Pattes Poulet".lower().split()
quantity = [randint(1,9) for x in range(len(item_name))]

dictionary = dict(zip(item_name,quantity))

print(dictionary)

for _ in range(5):
    ui = input("--> ").lower()
    if ui in dictionary:
        dictionary[ui] +=1
        print(dictionary)
    else:
        dictionary[ui] = 1
        print(dictionary)