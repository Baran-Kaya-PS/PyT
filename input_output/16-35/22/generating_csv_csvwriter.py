import csv
from tkinter.font import names

n = int(input())

with open("grades.csv","w",encoding="utf-8") as f:
    writer = csv.writer(f)

    writer.writerow(["Name","Score"])

    for i in range(1,n+1):
        name = input(f"Name of student {i}")
        score = input(f"Score of {name}")
        writer.writerow([name,score])

    f.close()

print("\n Content of 'grades.csv' :  ")

with open("grades.csv","r",encoding="utf-8") as f:
    print(f.read())