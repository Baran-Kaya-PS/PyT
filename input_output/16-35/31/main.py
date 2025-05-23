import os
import re

path = r"C:\Users\Baran\PycharmProjects\PythonCrashCourse\input_output"

def extract_files(path):
    items = os.listdir(path)
    return [f for f in items if os.path.isfile(os.path.join(path, f))]

def extract_dirs(path):
    items = os.listdir(path)
    return [d for d in items if os.path.isdir(os.path.join(path,d))]

def extract(path,dictionnary):
    files = extract_files(path)
    if files:
        for file in files:
            dictionnary[os.path.join(path,file)] = path
    dirs = extract_dirs(path)
    if dirs:
        for dir in dirs:
            extract(os.path.join(path,dir),dictionnary)
    return dictionnary

print(extract(path,{}))