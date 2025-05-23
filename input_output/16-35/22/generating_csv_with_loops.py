n = int(input("How much student you will add to the file : "))

data = {}



with open("new.csv","w",encoding="utf-8") as f:
    for x in range(1, n + 1):
        name = input(f"Name of the student {x} : ")
        grade = int(input("Grade of the student : "))
        f.write(f"{name},{grade}\n")