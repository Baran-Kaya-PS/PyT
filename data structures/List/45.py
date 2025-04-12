# 45. **Comparing Tuples**
#     Create two tuples.
#     Compare them with `<`, `>`, `==`.
#     Show how Python compares them element by element (lexicographically).
def int_to_letter(n):
    return chr(ord('a') + n)

from random import randint

t1 = tuple([int_to_letter(randint(0,25)) for _ in range(15)])
t2 = tuple([int_to_letter(randint(0,25)) for _ in range(15)])

print(t1)
print(t2)

print(t1>t2)
print(t1<t2)