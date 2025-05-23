# convert a tf to a json
import json

textfile_name = "file_x.txt"
jsonfile_name = "file_x.json"
records = []

with open(textfile_name,"r",encoding="utf-8") as fin:
    for raw_line in fin:
        if not raw_line.strip():
            continue

        name,age = raw_line.split()
        records.append({"name":name,"age":int(age)})

with open(jsonfile_name,"w",encoding="utf-8") as fout:
    json_text = json.dumps(records,ensure_ascii=False,indent=2)
    fout.write(json_text)

print(f"{len(records)} enregistrements écris dans {jsonfile_name}")