menu = {'Fried chicken': 10, 'Curry chicken': 12, 'Pizza': 20, 'Tea': 9, 'Coffee': 12, 'Hambagar': 23, 'Fried potato': 10, 'Beef': 30}

for i,j in menu.items():
    print(f'{i:15} is {j}$')

def resturant():
    total = 0
    while True:
        dish = input('Enter the name of the dish: ')
        if not dish:
            break
        try:
            total += menu.get(dish)
            print(f'{dish} costs {menu.get(dish)}, total is {total}')
        except:
            print('Typo error! Try another.')
    return f'Your total amount is {total}'

print(resturant())