l1 = "A B C D E F G".split()
l2 = [x+1 for x in range(7)]

dict = {}

for x in range(7):
    dict[l2[x]] = l1[x]

print(sorted(dict.items()))

del dict[1]

print(sorted(dict.items()))
