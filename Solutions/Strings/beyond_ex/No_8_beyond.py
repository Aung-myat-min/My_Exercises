def list_sort(be_list):
    li = be_list.split()
    return ','.join(sorted(li))

print(list_sort('Tom Dick Harry'))

def last_w(filename):
    with open(filename, 'r') as f:
        return list(f)[-1][-2]

print(last_w('sample3.txt'))

def longest(filename):
    with open(filename, 'r') as f:
        str = ''
        li = list(f)
        for i in li:
            for j in i.split():
                if len(str) < len(j):
                    str = j

        return str
print(longest('sample3.txt'))