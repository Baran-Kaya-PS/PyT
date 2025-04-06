l = []

for x in range(5):
    ui = input("--> ")
    l.append(ui)
print(l[::2]) # du premier élément au dernier avec saut de deux, si le saut dépasse la list c'est fini
print(l[2:5]) # du second au 5e élément avec u nsaut de 1.
