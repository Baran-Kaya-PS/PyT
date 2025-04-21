from random import randint

paq = {}

for x in range(10):
    quantity = randint(1,99)
    product_name = "product n°{}".format(x+1)
    paq[product_name] = quantity

# str.format()
for k,v in paq.items():
    print("({} | quantity = {})".format(k,v))

print()

#f-strings
for k,v in paq.items():
    print(f"({k} | quantity = {v})")
