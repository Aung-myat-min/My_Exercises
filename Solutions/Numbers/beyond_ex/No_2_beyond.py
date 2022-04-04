def mysum(*number_list):
    h = 0
    for i in number_list:
        h += i
    return h
def mysumb(number_list, arug = 0):
    try:
        arug + 1
    except:
        print('Invaild second arugment, it should be a number')
        return 1
    num = 0
    if len(number_list) < arug:
        for i in number_list:
            num += i
        num += arug
        return num
    else:
        for i in number_list[arug:]:
            num += i
        return num

def average(num_list):
    i = 0
    for l in num_list:
        i += l
    i = i/len(num_list)
    return i

def word_length(list):
    short = len(list[0])
    ave = 0
    long = len(list[0])
    for i in list:
        i = len(i)
        if i < short: short = i
        if i > long: long = i
        ave += i
    ave = ave/len(list)
    return [short, ave, long]

def every_sum(list):
    pass
