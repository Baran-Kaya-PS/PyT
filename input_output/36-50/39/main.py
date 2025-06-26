def head(fp,N):
    with open(fp,'r') as f:
        data = f.read(N)
        if data:
            print(data)
        else:
            print("file is empty")
