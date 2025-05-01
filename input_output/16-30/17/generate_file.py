# pip install faker lorem
from faker import Faker
import lorem
from random import randint

textfile_name = "file_x.txt"


def generate_sentence():
        fake = Faker()
        return fake.text(max_nb_chars=randint(5,89))

with open(textfile_name,"w",encoding="utf-8") as ntf:
    for x in range(500):
        sentence = generate_sentence()
        print(sentence)
        ntf.write(f"{sentence}\n")
