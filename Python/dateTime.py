import datetime

currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
year = date.strftime("%Y")

name = str(input('Enter your complete name: ')).title().strip().split()
while True:   
    try:
        yearOfBirth = int(input(f'{name[0]}, enter the year of your birth: '))
    except ValueError:
        print('ERRO: Please enter a valid year and try again.')
    else:
        print(f'{name[0]}, this year you will be {int(year) - yearOfBirth} years old.')
        break