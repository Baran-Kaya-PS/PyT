import datetime
import json
import os
path = r"C:\Users\Baran\PycharmProjects\PythonCrashCourse\input_output\36-50\38"
file_path = "tasks.json"

tasks = []

def init():
    if not os.path.exists(os.path.join(path,file_path)):
        with open("tasks.json","w") as f:
            json.dump([],f)
            return True
    return False

def add(description:str):
    ts = f"{datetime.datetime.now().replace(microsecond=0).isoformat()}"
    tasks.append({'created':ts,'task':description})
    print(f"Tache ajoutée : [{ts} : {description}]")

def list():
    pass


def load_tasks():
    with open("tasks.json", "r") as f:
        return json.loaf(f)

def save():
    buffer = load_tasks()
    for task in buffer:
        add(task)

    pass

def load():
    pass

def quit():
    pass

if __name__ == "__main__":
    print(init())
    