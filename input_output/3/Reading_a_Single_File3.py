with open("story.txt",'r',encoding="utf-8") as f:
    for line in f:
        if line.strip(): # supprime les espaces
            print(line,end="")