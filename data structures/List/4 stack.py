stack = []

def size():
    return len(stack)

def append(value):
    stack.append(value)

def pop():
    if size() >= 1:
        return stack.pop()
    return None

append(10)
append(20)
print(size())  # 2
print(pop())   # 20
print(size())  # 1
