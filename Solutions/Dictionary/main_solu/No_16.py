d1 = {'a':1, 'b':2, 'c':3}
d2 = {'a':1, 'b':2, 'c':4}
d3 = {'a':1, 'b':2, 'd':3}
d4 = {'a':1, 'b':2, 'c':4}
def dictdiff(a,b):
    f,g = sorted(a), sorted(b)
    difference = {}
    for i in f:
        c = []
        if a.get(i) != b.get(i):
            c.append(a.get(i))
            c.append(b.get(i))
            difference[i] = c
    for i in g:
        c = []
        if b.get(i) != a.get(i):
            c.append(a.get(i))
            c.append(b.get(i))
            difference[i] = c
    return difference

print(dictdiff(d4, d3))

