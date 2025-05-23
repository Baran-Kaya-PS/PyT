import json

with open("tasks.json","r",encoding="utf-8") as f:
    data = json.load(f)
    tasks = [task["title"] for task in data]
    ui = input(f"Quelles taches avez vous réalisé aujourd'hui ? {tasks} ")
    if ui not in tasks:
        print("flemmard")
        exit(0)
    else:
        for task in data:
            if task["title"] == ui:
                task["completed"] = True
    f.close()
with open("tasks.json","w",encoding="utf-8") as f:
    json.dump(data,f,indent=2)