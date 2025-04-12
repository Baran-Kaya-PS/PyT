# 44. **List Copy via Slicing**
#     Have a list of numbers.
#     Do `list2 = my_list[:]` for copying.
#     Modify `list2` and show that `my_list` is unaffected.
#     Compare it with a simple assignment `list2 = my_list`.
from random import randint

l = [randint(1,99) for x in range(15)]

l2 = l[:] # copy

for x in range(len(l2)):
    l2[x]+=randint(1,9)

print(l)
print(l2)

for val1,val2 in zip(l,l2):
    print(val2-val1)