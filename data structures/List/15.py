l = []

for x in range(5):
    ui = input("--> ")
    l.append(ui)

l2 = []

for x in range(5):
    ui = input("--> ")
    l2.append(ui)

l = tuple(l)
l2 = tuple(l2)
print(l<l2)
print(l>l2)
print(l == l2)