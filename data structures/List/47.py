# 47. **Splitting a List into Sublists**
#     Create a list with at least 10 elements.
#     Divide it into 2 or 3 sublists of approximately equal size with slicing.
#     Print each sublist.
from random import randint

l = [randint(1,99) for _ in range(12)]

l1 = l[0:4]
l2 = l[4:8]
l3 = l[8:12]

print(l1)
print(l2)
print(l3)