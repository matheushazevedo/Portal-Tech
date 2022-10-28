from time import sleep
from random import randint

password = randint(0, 10)
attempts = 3

while True:
    try:
        verifyPassword = int(input("\033[0;37mActivating the pump, enter the one-digit password: "))
        if verifyPassword == password:
            print(f"\033[0;32mAccess granted successfully. Starting countdown:")
            for i in range(10, 0, -1):
                print(f"\033[0;31mStarting the blast process in {i} {'seconds' if i > 1 else 'second'}.")
                sleep(1)
            print(f'\033[0;30mBoom!')
            break
        else:
            attempts -= 1
            print(f"\033[0;31mYou only have {attempts} more attempts.")
            print(f"The password is {'less' if verifyPassword > password else 'greater'} than {verifyPassword}.")
    except ValueError:
        attempts -= 1
        print(f"Enter numbers only. You only have {attempts} more attempts.")
    finally:
        if attempts == 0:
            print("\033[0;31mYou got it wrong, activating in 3 seconds.")
            for i in range(3, 0, -1):
                print(f"\033[0;30mStarting the blast process in {i} {'seconds' if i > 1 else 'second'}.")
                sleep(1)
            print(f'\033[0;30mBoom!')
            break