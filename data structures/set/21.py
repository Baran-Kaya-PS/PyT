l = "a a a a b c d e e e g g i k i i i i i i i i".split()
l2 = {}
ls = set(l)
for val in ls :
    l2[val] = l.count(val)

l2 = sorted(l2.items()) # tableau de paires
print(l2)