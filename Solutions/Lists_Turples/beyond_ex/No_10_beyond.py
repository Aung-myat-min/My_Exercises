def mysum_bigger_than(*numbers):
    num = 0
    for i in  numbers:
        if numbers[0] <= i:
            num += i
    return num

print(mysum_bigger_than(10,2,3,45,6,80))
print(sum((10,2,3,45,6,80)))

def sum_numeric(*numbers):
    num = 0
    for i in numbers:
        try:
            i + 16
        except:
            continue
        num += i
    return num

print(sum_numeric(10,'kkk', 10.3, 'hhh'))