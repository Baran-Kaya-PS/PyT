s1 = set("a b c d e f g".split())
s2 = set("a b c d e f g h i j k l m n o p".split())

print(sorted(s1.intersection(s2)))
print(sorted(s1.union(s2))) # ou s1 | s2