# Implement Queue using Stacks
# https://leetcode.com/problems/implement-queue-using-stacks/description/?envType=daily-question&envId=2024-01-29

class MyQueue:
    def __init__(self):
        self.my_queue = []

    def push(self, x: int):
        self.my_queue.append(x)

    def pop(self):
        return self.my_queue.pop(0)

    def peek(self):
        return self.my_queue[0]

    def empty(self):
        if len(self.my_queue) == 0:
            return True
        else:
            return False
