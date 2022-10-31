from calculater import calculater as cal

while True:
    print(f'\033[0;32m{" CALCULATER ":=^25}\033[0;37m')
    print('[1] Sum\n[2] Subtraction\n[3] Multiplication\n[4] Division\n[0] Exit')
    print(f'\033[0;32m{"-":=^25}\033[0;37m')
    while True:
        try:
            choice = int(input('Enter the number of one of the options above: '))
        except ValueError:
            print('\033[0;31mERROR: is not a valid integer, try again.\033[0;37m')
        else:
            if choice >= 0 and choice <= 4:
                break
            else: 
                print('\033[0;31mERROR: is not a valid option number, please try again.\033[0;37m')
                continue
    if choice == 0: break
    while True:
        try:
            fNumber = float(input('Enter the first number: '))
        except ValueError:
            print('\033[0;31mERROR: is not a valid integer, try again.\033[0;37m')
        except Exception as erro:
            print(erro)       
        else:
            break
    while True:
        try:
            sNumber = float(input('Enter the second number: '))
        except ValueError:
            print('\033[0;31mERROR: is not a valid integer, try again.\033[0;37m')
        except Exception as erro:
            print(erro)
        else:
            if sNumber == 0 and choice == 4:
                print('\033[0;31mERROR: cannot divide by zero, try again.\033[0;37m')
                continue
            else: break

    match choice:
        case(1):
            result = [cal(fNumber, sNumber, '+'), '+']
        case(2):
            result = [cal(fNumber, sNumber, '-'), '-']
        case(3):
            result = [cal(fNumber, sNumber, '*'), '*']       
        case(4):
            result = [cal(fNumber, sNumber, '/'), '/']
    print(f'{fNumber:.2f} {result[1]} {sNumber:.2f} = {result[0]:.2f}')
    
print('Program completed successfully.')