def clean(line):
    return line.rstrip("\n")

def process_line(line):
    return line[::-1]

def apply_to_file(path):
    with open(path,'r',encoding="utf-8") as f:
        for lineno,raw in enumerate(f,start=1):
            cleaned = clean(raw)
            print(f"{lineno} : {process_line(cleaned)} : {cleaned}")

apply_to_file("input.txt")