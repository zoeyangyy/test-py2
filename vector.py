import numpy as np

class Vector2(object):
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%s, %s)" % (self.x, self.y)

    def from_points(self, P1, P2):
        self.x = P2[0]-P1[0]
        self.y = P2[1]-P1[1]
        return self

A = (10.0, 20.0)
B = (30.0, 35.0)
vec = Vector2()
AB = vec.from_points(A, B)
print(AB)

