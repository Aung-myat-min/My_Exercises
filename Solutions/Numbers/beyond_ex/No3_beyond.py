def run_timing():
    name = input("Your name: ")
    numbers_of_run = 0.0
    kilometers = 0.0
    while True:
        print("Enter how long do you take to run 10km")
        tot = input(":: ")
        if tot:
            kilometers += float(tot)
            numbers_of_run += 1.0
        if not tot:
            print(f"{name.title()}, That is your result.")
            print(f"Average of {kilometers/numbers_of_run}, {int(numbers_of_run)}runs")
            break

def float_converter(flo, start = 0, end = None):
    floats = str(flo)
    li = floats.split('.')
    if end == None:
        ans = li[0][-start:]+'.'+li[1][:]
    else:
        ans = li[0][-start:] + '.' + li[1][:end]
    return float(ans)

print(float_converter(1234.5678))