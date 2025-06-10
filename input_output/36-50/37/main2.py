import os


def extract(path):
    for root, dirs, files in os.walk(path):
        txt_files_path = [os.path.join(root,f) for f in files if f.endswith(".txt")]
        for filepath in txt_files_path:
            with open(filepath,'r') as curr_file:
                for count,line in enumerate(curr_file,start=1):
                    pass
                print(f"file {filepath} have {count} lignes")


if __name__ == '__main__':
    print(extract(r"C:\Users\Baran\PycharmProjects\PythonCrashCourse\input_output\36-50\37"))