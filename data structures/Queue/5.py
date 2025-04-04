from collections import deque

def new_deque():
    nd = deque()
    return nd

nd = new_deque()
for i in range(3):
    nd.appendleft(input("Insérer un élément à gauche : "))
    nd.append(input("Insérer un élément à droite : "))
print(nd)
print(nd.pop())
print(nd.popleft())
print(nd)