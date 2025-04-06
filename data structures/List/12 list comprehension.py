from random import randint

n = 10
l = []
# # [expression for élément in iterable if condition]
# print(l)

for i in range(n):
    l.append(randint(-9,9))
print(l)

pl = [x for x in l if x > 0]
nl = [x for x in l if x <= 0]

print(pl,nl)