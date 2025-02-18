# Déplace chaque lettre d'une phrase de trois places dans l’alphabet (chiffrement César).
# shift every char from 97 to 122

low_ord = 97
max_ord = 122

user_input = input("-->").lower()

def cesar(input,shift):
    processed = ""
    special_chars = [" ",",",";","!","?","'"]
    for ch in input:
        if ch in special_chars:
            processed+=ch
        else:
            ord_val = ord(ch)
            ord_val = ord_val+shift
            if ord_val > 122:
                ord_val = (ord_val%122)+97
            processed += chr(ord_val)
    return processed

shift3 = (cesar(user_input,3))
original = (cesar(shift3,-3))

print("shift3 : ",shift3)
print("original : ",original)
