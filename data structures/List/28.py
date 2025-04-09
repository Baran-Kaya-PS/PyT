l = "A B C D E F G H I J K".split()

for index,data in enumerate(l,start=1):# au lieu de faire index+1 on peux faire start = x
    print(str(index)+" "+ str(data))