import json
import os

listdir = os.listdir()

json_files = [json_file for json_file in listdir if json_file.endswith(".json")]

concat = []

for file in json_files:
    with open(file,"r") as f:
        buffer_data = json.load(f)
        # print(f"fichier {file} : {buffer_data}")
        for data in buffer_data:
            person = {'name':data['name'],'id':data['id']}
            concat.append(person)
concat = sorted(concat,key=lambda x: x['id'])

with open("concat.json", "w") as f:
    json.dump(concat, f, indent=2)
