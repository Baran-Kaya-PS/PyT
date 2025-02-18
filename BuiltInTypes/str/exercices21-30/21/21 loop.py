def is_digit2(ch):
    numbers = [0,1,2,3,4,5,6,7,8,9]
    intValue = ord(ch) - ord('0')
    if intValue in numbers:
        return True
    return False

isDigit = True

user_input = input("-->")
for ch in user_input:
    if not is_digit2(ch):
        isDigit = False
print(isDigit)



