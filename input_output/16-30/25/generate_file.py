from faker import Faker
import lorem
from random import randint

textfile_name = "lines.txt"

def generate_sentence():
    fake = Faker()
    return fake.text(max_nb_chars=randint(5,50))

with open(textfile_name,"w",encoding="utf-8") as f:
    for x in range(15):
        s = generate_sentence().replace(".","")
        f.write(f"{s}\n")