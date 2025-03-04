import keyword
from keyword import kwlist
isValid = True
def is_keyword(s):
    return s in keyword.kwlist
user_input = input()
if is_keyword(user_input):
    isValid = False
elif user_input[0].isdigit():
    isValid = False
else:
    for ch in user_input:
        if not (ch.isalnum() or ch == "_"): # or if not ch.isalnum() and not ch =="_") DeMorgan laws
            isValid = False
print(isValid)