l = []
for x in range(5):
    l.append(x+1)

l.insert(0,int(input("--> ")))
l.insert(len(l),int(input("--> ")))

print(l)