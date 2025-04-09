l1 = "A B C D E F G H I J K".split()
l2 = "1 2 3 4 5 6 7 8 9 10 11".split()
l3 = "Zip permet de manipuler plusieurs objets dans une loop".split()

for x,y,z in zip(l1,l2,l3):
    print(x,y,z)
