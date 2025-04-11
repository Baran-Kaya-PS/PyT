# 39. **Error Handling with `list.index()`**
#     Have a list.
#     Ask the user for a value to find.
#     Use a `try/except` block for `list.index()`.
#     If found, print the index; if not, display an error message.

l = "a b c d e f g h i j k l m".split()
print(l)
try:
    ui = input("-->")
    print(l.index(ui)+1)
except:
    print("Value does not exist")