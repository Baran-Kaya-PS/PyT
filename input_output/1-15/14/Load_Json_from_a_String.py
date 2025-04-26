import json

data = dict(json.loads('{"username": "alice", "active": true, "score": 42}'))

for k,v in data.items():
    print(f"{k} is the key, {v} is the value\n")

data_list = list(json.loads('{"username": "alice", "active": true, "score": 42}').values())

print(data_list)