# 40. **Conditional Deletion in a List**
#     Have a list of numbers.
#     Loop and remove every negative number.
#     Discuss the trap of modifying the list while iterating.
#     Show why it’s safer to build a new filtered list instead.

l = [1,2,7,8,2,3,1,94,-22,-2,-99,-4153]

for val in l[:]: # copie de la liste car si on supprime des valeurs pendant l'itération on décale les valeurs => problème
    if val<0:
        l.remove(val)
print(l)

l = [1,2,7,8,2,3,1,94,-22,-2,-99,-4153]

l = [x for x in l if x > 0]

print(l)