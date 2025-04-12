# 42. **List of Tuples and MultiLevel Sorting**
#     Have tuples `(title, price, quantity)`.
#     First sort by `price`, then by `quantity` if prices are equal.
#     Use an appropriate `lambda` or a function returning `(price, quantity)`

data = [
    ("Eau", 0.75, 20),
    ("Lait", 1.20, 15),
    ("Beurre", 2.20, 10),
    ("Semoule", 1.10, 8),
    ("Riz", 0.95, 25),
    ("Pâtes", 0.85, 30),
    ("Poulet", 5.40, 12),
    ("Farine", 1.00, 18),
    ("Sucre", 1.30, 14),
    ("Œufs", 2.20, 16)
]

data = sorted(data,key=lambda x:[-x[1],x[2]]) # -x[k] reverse the sort on the kth data

print(data)