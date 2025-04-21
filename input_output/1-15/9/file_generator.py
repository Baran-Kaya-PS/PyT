def int_to_alphabetic_char(val):
    return chr((ord('a')+val))

from random import randint

textfile_name = "file_x.txt"
with open(textfile_name,"w",encoding="utf-8") as ntf:
    for y in range(100):
        ch = int_to_alphabetic_char(randint(0,25))
        print(ch + " has been added to the file")
        ntf.write(f"{ch}\n")