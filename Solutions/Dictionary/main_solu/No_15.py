def get_rainfall():
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
            record[rainfall] = amount
        else:
            a = record.get(rainfall) + amount
            record[rainfall] = a
    return record

print(get_rainfall())