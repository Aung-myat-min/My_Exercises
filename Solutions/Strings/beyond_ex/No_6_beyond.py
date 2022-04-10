def print_nth(filename):
    with open(filename, 'r') as f:
        sentences = list(f)
        for i in range(10):
            print(sentences[i][i])

def transpose(a_list):
    real_ans = []
    ans = []
    he_str = ''
    fake_ans = []
    range_num = len(a_list[0].split())
    for i in a_list:
        i = i.split(' ')
        fake_ans.append(i)
        if len(i) != range_num:
            print('The length of the lists are not equal.')
            return 1
        else:
            continue
    for i in fake_ans[0]:
        real_ans.append([i])
    for j in fake_ans[1:]:
        num = 0
        for i in j:
            real_ans[num].append(i)
            num += 1
        num = 0
    for i in real_ans:
        for j in i:
            he_str += j + ' '
        ans.append(he_str.rstrip())
        he_str = ''
    return ans

print(transpose(['abc def ghi', 'jkl mno pqr', 'stu vwx yz']))
