with open("file_x.txt","wb+") as f:
    f.write(b'\x00' * 20)
    f.seek(9) #déplace le curseur / pointeur
    f.write(b"ABCDE")
    f.seek(0)
    print(f.read())