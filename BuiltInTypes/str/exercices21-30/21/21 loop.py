user_input = input("-->")
is_digit = True
for ch in user_input:
    if not ch.isdigit(): is_digit = False
print(is_digit)