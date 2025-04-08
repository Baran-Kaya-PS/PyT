from random import randint

l = [x+randint(-3,5) for x in range(10)]
l1 = l.copy()
l1.sort(reverse=True) # tri dans le sens inverse
l2 = l.copy()
l2.reverse() # inverse la liste

print(l)
print(l1)
print(l2)