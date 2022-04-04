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

run_timing()