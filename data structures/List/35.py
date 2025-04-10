# 35. **Custom Sort with `key`**
#     Have a list of tuples `(name, age)`.
#     Sort it by age using `list.sort(key=lambda x: x[1])`.
#     Print the list after sorting.

l = [("Brian", 13), ("Andy", 14), ("Mcdonald", 59), ("Christopher", 42), ("Ryan", 11)]


l.sort(key=lambda x: x[1])

print(l)

l1 = "Brian Andy Mcdonald Christopher".split()
l2 = [13,14,59,42]

l3 = list(zip(l1, l2))
print(l3)