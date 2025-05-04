# functional version of the main
import json


def parse_line(line):
    name,age = line.strip().split()
    return {"name":name,"age":int(age)}

with open("file_x.txt","r",encoding="utf-8") as fin:
    lines = filter(str.strip,fin)
    records = list(map(parse_line,lines))

with open("file_x.json","w",encoding="utf-8") as fout:
    json.dump(records,fout,ensure_ascii=False,indent=2)
print(f"{len(records)} enregistrements écris")
