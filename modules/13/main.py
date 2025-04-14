from random import randint

def int_to_letter(n):
    return chr(ord('a')+n)

from libs import * #import mod_(a,b,d) et pas c
w = []
for _ in range(10):
    w.append(int_to_letter(randint(0,25)))
print(mod_a.fun_a(str(w)))
print(mod_b.fun_b(str(w)))
print(mod_d.fun_d(str(w)))

try:
    print(mod_c.fun_c(w))
except:
    print("module non importé")