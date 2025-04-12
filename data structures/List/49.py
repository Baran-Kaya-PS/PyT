# 49. **Using `zip()` with Multiple Arguments**
#     Have three lists of the same length.
#     Loop over them simultaneously with `zip(l1, l2, l3)`.
#     For each index, print the combination of the three elements.
from random import randint

l1 = [randint(1,9) for _ in range(3)]
l2 = [randint(10,99) for _ in range(3)]
l3 = [randint(100,999) for _ in range(3)]
max_value = 0
for v1,v2,v3 in zip(l1,l2,l3):
    val = v1+v2+v3
    print(val)
    if max_value < val :
        max_value = val
print("valeur maximale :",max_value)