s1 = set("1 2 3 4 5 6 7 8 9 10".split())
s2 = set("5,6,8,10,13,14,1567,13")

print(s1-s2) # s1 - elements communs de s2
print(s2-s1) # s2 - elements communs de s1

print(sorted(s1^s2))
print(sorted(s2^s1))

print(sorted((s1|s2)))
print(sorted((s2|s1)))
