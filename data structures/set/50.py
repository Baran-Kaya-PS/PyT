# 50. **Manually Merging Multiple Sets**
#     Request three sets from the user (typed as spaceseparated strings).
#     Convert them all to Python `set` objects.
#     Print the final merged set (`set1 | set2 | set3`).
#     Optionally show the global intersection, too.


s1 = set("chat chien oiseau".split())
s2 = set("chien souris".split())
s3 = set("perroquet chat dauphin".split())

print("Set 1 :", s1)
print("Set 2 :", s2)
print("Set 3 :", s3)

print(s1|s2|s3)