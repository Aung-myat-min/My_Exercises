def hex_output():
    integer = 0
    hex = input("Enter the hex_number to convert: ")

# In this exercise, I was a little confused about hex so I watched the solution and wrote this solution.

    for power, i in enumerate(reversed(hex)):
        integer += int(i, 16) * int(16 ** power)
        print(integer)
    return (print(integer))


def name_tri():
    name = input('Enter your name: ')
    name = name.upper()
    spaces = len(name)/2
    index = 1
    for i in range(len(name)):
        i = i+1
        stri = ' '*int(spaces-i/2)
        print(stri + name[:index] + stri)
        index += 1

name_tri()
