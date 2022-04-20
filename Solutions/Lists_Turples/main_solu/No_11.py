PEOPLE = [{'first':'Reuven', 'last':'Lerner',
            'email':'reuven@lerner.co.il'},
            {'first':'Donald', 'last':'Trump','email':'president@whitehouse.gov'},
            {'first':'Vladimir', 'last':'Putin',
            'email':'president@kremvax.ru'}
            ]

def alphabetize_names(peopel_names):
    al_dict = {}
    names = []
    name = ''
    returning = []
    for i in peopel_names:
        name += i['last'] + ' ' + i['first']
        names.append(name)
        al_dict[name] = i
        name = ''
    names = sorted(names)
    for k in names:
        returning.append(al_dict[k])
    return returning

print(alphabetize_names(PEOPLE))
