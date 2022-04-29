def get_rainfall_average():
    record = {}
    while True:
        rainfall = input(': ')
        if not rainfall: break
        try:
            amount = int(input(f'{rainfall} rainfall times?: '))
        except:
            print('It is not a number')
            continue
        if not rainfall in record.keys():
            record[rainfall] = [amount, 1]
        else:
            a = record.get(rainfall)[0] + amount
            record[rainfall] = [a, record.get(rainfall)[1]+1]
    for k,v in record.items():
        print(f'{k} has {v[0]} rain(s)')
        print(f'Its average is {v[0]/v[1]}')

def telling_words(file):
    with open(file, 'r') as f:
        a_dict = {}
        for i in f:
            for j in i.split():
                a = f'{len(j)} letter word(s)'
                a_dict[a] = a_dict.get(a, 0) + 1
    return a_dict
