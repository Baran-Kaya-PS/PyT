import filecmp

with open("file_x.txt","rb") as src, open("copy.bin","wb") as dst:
    while True:
        chunk = src.read(1024)
        if not chunk:
            break
        dst.write(chunk)

identiques = filecmp.cmp("file_x.txt","copy.bin",shallow=False)
print(identiques)