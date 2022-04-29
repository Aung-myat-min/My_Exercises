i = {'a': 1, 'b': 2}
g = {'c': 3, 'b': 3}
h = {'b': 4, 'd': 16}
def merge_dict(*dic):
    return_dict = {}
    for i in dic:
        return_dict.update(i)
    return return_dict

def any_to_dict(*arugs):
    au = {}
    for i in range(0,len(arugs), 2):
        au[arugs[i]] = arugs[i+1]
    print(au)
any_to_dict(1,2,3,4)

##Need one more exercise