from random import randint
import json
from faker import Faker
from Person import *


fake = Faker()
Persons = []

for x in range(50):
    Persons.append(Person(fake.name().split()[0],randint(15,99)))

dict_list = [p.encode_in_dict() for p in Persons]

print(dict_list)

with open("Persons.json","w") as f:
    json.dump(dict_list,f)