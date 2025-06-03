import json

logs = []

def add_log(data, lineno):
    logs.append({'data':data,'lineno':lineno})

Persons = []


def isValid(person):
    return (isinstance(person.get('name'),str) and
            isinstance(person.get('age'),int) and
            isinstance(person.get('city'),str))


def write_logs(item, lineno):
    print(f"error with the line {lineno} : {item}")

with open("data.json","r") as f:
    data = json.load(f)
    for lineno, item in enumerate(data,start=1):
        try:
            person = {'name': item['name'], 'age': int(item['age']), 'city': item['city']}
            if isValid(person):
                Persons.append(person)
            else :
                add_log(item,lineno)
                write_logs(item, lineno)
        except:
            write_logs(item,lineno)
            add_log(item, lineno)

if logs:
    with open("err_lol.txt","w",encoding="utf-8") as logfile:
        for log in logs:
            logfile.write(f"Line {log['lineno']} : {log['data']}\n")