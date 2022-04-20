def sort_by_absd(numbers):
    return sorted(numbers, key=abs)

print(sort_by_absd([-9,10,1,3,-2,-4,5,6]))

def sort_by_vow(words):
    dic = {}
    for i in words:
        count = 0
        for j in i:
            if j in list('aeiou'):
                count += 1
        dic[i] = count
    ha = dict([k,v] for v,k in dic.items())
    ha = ha.get(sorted(ha, reverse=True)[0])
    return ha
print(sum([1,2,3]))
print(sort_by_vow(['apple', 'eye', 'aaaa', 'uility']))

def sort_sum(lists_of_num):
    dic = {}
    for i in lists_of_num:
        dic[str(i)] = sum(i)
    ha = dict([k,v] for v,k in dic.items())
    ha = ha.get(sorted(ha, reverse=True)[0])
    return ha

print(sort_sum([[0,1], [9.1], [90,9]]))
