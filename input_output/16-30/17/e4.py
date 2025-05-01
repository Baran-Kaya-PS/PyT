with open("copy.bin","r",encoding="utf-8") as f:
    buffer = ""
    count = 0
    while count < 10:
        chuck = f.read(1024)
        if not chuck:
            break
        buffer += chuck
        parts = buffer.split(".")
        for sent in parts[:-1]:
            print(sent+ ".")
            count+=1
            if count == 10:
                break