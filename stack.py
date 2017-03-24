# -*- coding: utf-8 -*-


class Stack:
    def __init__(self, size):
        self.stack = []   # 列表
        self.size = size
        self.top = -1

    def push(self, content):
        if self.Full():
            print "stack is full"
        else:
            self.stack.append(content)
            self.top += 1

    def pull(self):
        if self.Empty():
            print "stack is empty"
        else:
            self.stack.pop()
            self.top -= 1

    def Full(self):
        if self.top == self.size:
            return True
        else:
            return False

    def Empty(self):
        if self.top == -1:
            return True
        else:
            return False

q = Stack(7)
print q.Empty()

q.push('a')
q.push('b')
q.pull()
print q.stack
