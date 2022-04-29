import datetime
import pickle


def account():
    import pickle as pi
    with open('file.pkl', 'rb') as f:
        file = {}
        try:
            file = pi.load(f)
            print(file)
        except EOFError:
            pass

        def login():
            print('Fill up your name: ')
            name = input(': ')
            print('Fill your password: ')
            password = input(': ')
            if file.get(name) == password:
                print('Successfully Loged in')
            else:
                print('Wrong password!')

        def sign_up():
            rname = ''
            rpassword = ''
            while True:
                print('Enter your name: ')
                name = input(': ')
                if name in file.keys():
                    print('Name already taken')
                    continue
                else:
                    rname += name
                    break
            while True:
                print('Enter your password:')
                password = input(': ')
                print('Rewirte password again:')
                repassword = input(': ')
                if not password == repassword:
                    print('Doesn\'t match')
                    continue
                else:
                    rpassword += password
                    break

            file[rname] = rpassword

        while True:
            print('Login or Sign_up?')
            pro = input(': ')
            if not pro:
                break
            if pro == 'Login':
                login()
            elif pro == 'Sign_up':
                sign_up()
        with open('file.pkl', 'wb') as f:
            pi.dump(file, f)


'''
import datetime, random

date = datetime.datetime(2020,4,16)
dates = [date+datetime.timedelta(days=x) for x in range(365)]
temperatures = []
for i in range(365): temperatures.append(random.randint(22,35))
di = {}
for i in range(365): di[dates[i]] = temperatures[i]
with open('data.pkl' , 'wb') as f:
    pickle.dump(di,f)'''


def asking_temperature():
    with open('data.pkl', 'rb') as f:
        f = pickle.load(f)
        print('Ask the temperature of the days from 16.4.2020 to 16.4.2021')
        i = input('yyyy mm dd: ').split()
        temget = datetime.datetime(int(i[0]), int(i[1]), int(i[2]))
        return f.get(temget)

def asking_age():
   Family = {'DNS': datetime.date(1978, 1, 1),
             'UMKKM': datetime.date(1977, 7, 7),
             'NMKK': datetime.date(2005, 4, 16),
             'AMM': datetime.date(2005, 3, 20),
             'NBL': datetime.date(2008, 11, 21)}
   ask = input('Enter the name: ')
   a = Family.get(ask)
   age = datetime.date.today() - a
   print(f'{ask} is born on {a} and {ask} is {round(age.days/365)}years old.')

asking_age()


