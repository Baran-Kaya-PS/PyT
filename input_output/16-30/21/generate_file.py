from faker import Faker

fake = Faker("en_US")

data = "\n".join(fake.words(nb=50000))

with open("file_x.txt","w",encoding="utf-8") as f:
    f.write(data)
    f.close()