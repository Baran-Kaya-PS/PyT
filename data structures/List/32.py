# 32. **List of Lists and Nested List Comprehensions**
#     Create a list of lists (a small matrix).
#     Using a **nested list comprehension**, extract only the even elements.
#     Print the result.

m = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

l = [val for ligne in m for val in ligne if val % 2 != 0]

print(l)