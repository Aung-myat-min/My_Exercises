import shutil
from io import StringIO

def square(num_or_float):
    return num_or_float * num_or_float

print(square(23))
print(square(2.2))

def largest(not_num):
    return max(max(not_num))[0]

print(largest('atoz'),
      largest(['hh', 'hhhh', 'hz']),
      largest(('kk', 'll', 'oz')))

def largest_in_both(filename):
    buf = StringIO()
    if '.txt' in filename:
        with open(filename, 'r') as f:
            str = ''
            li = list(f)
            for i in li:
                for j in i.split():
                    if len(str) < len(j):
                        str = j
        return str
    else:
        with open(filename, 'r') as f:
            buf.seek(0)
            shutil.copyfileobj(buf, f)
            li = list(f)
            for i in li:
                for j in i.split():
                    if len(str) < len(j):
                        str = j
        return str

def odd_even(numbers):
    odd = sum(i for i in numbers[::2])
    even = sum(i for i in numbers[1::2])
    return [odd , even]

print(odd_even([1,2,3,4,5]))

def sub_add(numbers):
    num = 0
    add = True
    for i in numbers:
        if add:
            num += i
            add = False
        else:
            num -= i
            add = True
    return num

print(sub_add([10,2,3,4,5]))

def zipp(lists, str):
    count = max([len(lists), len(str)])
    turs = []
    for i in range(count):
        try:
            a = lists[i]
            turs.append((a, str[i]))
        except:
            turs.append((str[i]))
    if len(lists) != len(str):
        print('some interator(s)')
        print(turs)
    else:
        print('no interator')
        print(turs)

zipp(['a', 'b' ,'c'], '123')
