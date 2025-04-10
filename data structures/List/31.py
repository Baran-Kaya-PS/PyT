# 31. **Queue with `list`**
#     Discuss the inefficiency of `pop(0)` in a list.
#     Show a queue implementation using a list (removing from index(0)).
#     Display the impact on the list size if you do many operations.
#     Every function are given, i just implement pop(self,index)
class Stack:
    def __init__(self):
        # Internal list to store stack elements
        self.items = []

    def push(self, item):
        # Add item to the TOP (end) of the stack
        self.items.append(item)

    def pop(self):
        # Remove item from the TOP (end) of the stack
        if not self.is_empty():
            return self.items.pop()
        return None  # or raise an exception

    def peek(self):
        # Return the top element without removing it
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def dequeue(self,index):
        if not len(self.items) == 0:
            return self.items.pop(0)
