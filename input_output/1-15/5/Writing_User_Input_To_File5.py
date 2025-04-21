text = input("--> ")

with open("new.txt", "w", encoding="utf-8") as nt:
    nt.write(text)