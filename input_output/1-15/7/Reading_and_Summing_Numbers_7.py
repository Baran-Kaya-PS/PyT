def sum_file():
    textfile_name = input("Choissisez le nom du fichier : ").strip()
    try:
        with open(textfile_name, 'r', encoding="utf-8") as tf:
            sum_ = 0
            for line in tf:
                value = int(line.strip())
                sum_ += value
    except FileNotFoundError:
        print(f"File does noes exist : {textfile_name!r}")
        return None
    except ValueError:
        print(f"le fichier {textfile_name} contient des types non entiers")
        return None
    return sum_


sum_ = sum_file()
print(sum_)