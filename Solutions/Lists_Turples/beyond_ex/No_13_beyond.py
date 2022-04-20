MOVIES = [('Titanic', 150, 'Michal'),
          ('Big Bang', 120, 'David'),
          ('Neuron', 110, 'Khaled'),
          ('The', 90, 'Jame'),
          ('Kol', 160, 'AMM')]

def sort_by_user():
    print('''Options::  Length
           Name
           Director''')
    opt = input('::')
    mar = {'Name': 0, 'Length': 1, 'Director': 2}
    sample = {}
    for i in MOVIES:
        sample[i[mar.get(opt)]] = i
    re = sorted(sample)
    for i in re:
        print(sample.get(i))


def sort_by_user2():
    print('''Options::  Length
           Name
           Director''')
    opt = input('::').split()
    mar = {'Name': 0, 'Length': 1, 'Director': 2}
    sample = {}
    for i in opt:
        sa = {}
        for j in MOVIES:
            sa[j[mar.get(i)]] = j
        re = sorted(sa)
        print(f'By {i}')
        for k in re:
            print(sa.get(k))

sort_by_user2()
