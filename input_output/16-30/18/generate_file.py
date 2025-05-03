from faker import Faker
from random import randint

textfile_name = "file_x.txt"

def generate_name():
    fake = Faker()
    return fake.name().split()[0]

with open(textfile_name,"w",encoding="utf-8") as f:
    for x in range(int(input())):
        f.write(f"{generate_name()} {randint(15,99)}\n")
