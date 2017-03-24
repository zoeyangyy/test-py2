# -*- coding: utf-8 -*-


class Queue:
    def __init__(self, size):
        self.queue = []
        self.size = size
        self.head = -1
        self.tail = -1

    def Empty(self):
        if self.head == self.tail:
            return True
        else:
            return False

    def Full(self):
        if self.tail - self.head == self.size:
            return True
        else:
            return False

    def enQueue(self, content):
        if self.Full():
            print "queue is full"
        else:
            self.queue.append(content)
            self.tail += 1

    def outQueue(self):
        if self.Empty():
            print "queue is empty"
        else:
            self.head += 1


que = Queue(3)
print que.Empty()
que.enQueue('apple')
que.enQueue('pine')
que.enQueue('applepine')
print que.Full()
que.outQueue()
que.outQueue()
print que.queue[que.head + 1]
