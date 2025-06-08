import os

dir = ""

#méthode 1

def extract_files(path):
    items = os.listdir(path)
    return [f for f in items if os.path.isfile(os.path.join(path, f)) and f.endswith(".txt")]

def count_lines(file,path):
    fp = os.path.join(path,file)
    with open(fp,'r') as f:
        line_count = f.read().count('\n')
        return f"path {path}, File {file} have {line_count} lines"

def extract_dirs(path):
    items = os.listdir(path)
    return [d for d in items if os.path.isdir(os.path.join(path,d))]

def extract(path):
    files = extract_files(path)
    if files:
        for file in files:
            print(count_lines(file,path))
    dirs = extract_dirs(path)
    if dirs:
        for dir in dirs:
            extract(os.path.join(path,dir))
if __name__ == '__main__':
    extract(r"C:\Users\Baran\PycharmProjects\PythonCrashCourse\input_output\36-50\37")

