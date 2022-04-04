def hex_output():
    integer = 0
    hex = input("Enter the hex_number to convert: ")
## In this exercise, I was a little confused about hex so I watched the solution and wrote this solution.
    for power, i in enumerate(reversed(hex)):
        integer += int(i, 16) * int(16 ** power)
        print(integer)
    return (print(integer))

