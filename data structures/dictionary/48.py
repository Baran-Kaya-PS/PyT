# 48. **Dictionary Comprehension**
#     Ask the user for an integer `n`.
#     Build a dictionary `{x: x*x for x in range(n)}`.
#     Print it.

n = 50

dictionary = {x: x*x for x in range(n)} # soit {key : value for...}
print(dictionary)