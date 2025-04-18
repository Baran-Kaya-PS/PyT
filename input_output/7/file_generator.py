from random import randint

for x in range(5):
    textfile_name = "file_"+str(x)
    with open(textfile_name,"w",encoding="utf-8") as ntf:
        for y in range(100):
            val = randint(-50,150)
            ntf.write(f"{val}\n")