def ubbi_dubbi(inputs):
    inputs = inputs.lower()
    real_ans = ''
    for i in inputs:
        if i in list('aeiou'):
            real_ans += 'ub' + i
        else:
            real_ans += i

    print(real_ans)

ubbi_dubbi('octopus')