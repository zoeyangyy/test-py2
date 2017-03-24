generator = (x*x for x in range(3))
for x in generator:
    print x


def yieldfuc():
    for x in range(3):
        yield x*x

mygener = yieldfuc()
print mygener
for i in mygener:
    print i

