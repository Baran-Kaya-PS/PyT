from collections import deque


def head(fp:str,n:int=10) -> None:
    with open(fp,encoding='utf-8') as f:
        for _ in range(n):
            line = f.readline()
            if not line:
                break
            print(line,end="")

def tail(fp,n:int=10)-> None:
    with open(fp,encoding='utf-8') as f:
        for line in deque(f,maxlen=n):
            print(line,end="")