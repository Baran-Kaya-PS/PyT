# 34. **Advanced Filtering**
#     Make a list of numbers that includes some `None` values and negative numbers.
#     Use a list comprehension to filter out only the non`None` and positive ones.
#     Print the final filtered list.

l = [1,2,None,34,121,None,None,None,44,-765]

l =  [x for x in l if x is not None]

print(l)