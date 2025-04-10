# 33. **Matrix Transposition**
#     Reuse the concept of a matrix (e.g., 3×4).
#     Transpose it with `[[row[i] for row in matrix] for i in range(...)]`.
#     Compare that with `zip(*matrix)`.

l = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12]
]

l2 = [[row[i] for row in l] for i in range(len(l[0]))]
print(l2)

l2 = []

for i in range(len(l[0])):
    new_row = []
    for row in l:
        new_row.append(row[i])
    l2.append(new_row)
print(l2)

l2 = list(zip(*l))  # Donne des tuples
l2 = [list(row) for row in l2]  # Convertit en listes pour garder le même format
print(l2)
