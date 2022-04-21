from collections import namedtuple

guide = namedtuple('Moive', 'Name Length Director')
MOVIES = [guide('Titanic', 150, 'Michal'),
         guide('Big Bang', 120, 'David'),
         guide('Neuron', 110, 'Khaled'),
         guide('The' , 120, 'Trump'),
         guide('Kol', 160, 'AMM')]
print(MOVIES)
print([sorted(MOVIES[i].Name for i in range(5))])
def sort_by_user():
    print('''Options::  Length
           Name
           Director''')
    opt = input('::')
    sample = {}
    for i in MOVIES:
        g = None
        if opt == 'Name':
            g = i.Name
        elif opt == 'Length':
            g = i.Length
        else:
            g = i.Director
        sample[g] = i
    re = sorted(sample)
    for i in re:
        print(sample.get(i))

def sort_by_user2():
    print('''Options::  Length
           Name
           Director''')
    opt = input('::').split()
    sample = {}
    for i in opt:
        sa = {}
        for j in MOVIES:
            g = None
            if i == 'Name':
                g = j.Name
            elif i == 'Length':
                g = j.Length
            else:
                g = j.Director
            sa[g] = j
        re = sorted(sa)
        print(f'By {i}')
        for k in re:
            print(sa.get(k))

sort_by_user2()
