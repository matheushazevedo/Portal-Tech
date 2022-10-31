def calculater (firstNumber:float, secondNumber:float, operation:str):
    """This function will calculate two values ​​in the same order (firstNumber and secondNumber) considering the operations of addition, subtraction, multiplication and division. 
    
    Arguments:
        firstNumber (float): First number to be used for calculation.
        secondNumber (float): Second number to be used for calculation.
        operation (str): Describe which operation you want to use in this operation.
    """

    match operation:
        case('sum'):
            result = firstNumber + secondNumber
        case('subtraction'):
            result = firstNumber - secondNumber
        case('multiplication'):
            result = firstNumber * secondNumber
        case('division'):
            result = firstNumber / secondNumber

    return result


while True:
    try:
        firstNumber = float(input('Enter the first number: '))
    except:
        print('Please check and try again.')
    else:
        break
while True:
    try:
        secondNumber = float(input('Enter the second number: '))
    except:
        print('Please check and try again.')
    else:
        break
while True:
    operation = str(input('Enter the operation that is: ').lower())
    if operation == 'sum' or operation == 'subtraction' or operation == 'multiplication' or operation == 'division':
        break
    else:
        print('Please check and try again.')

print(f'The {operation} of {firstNumber:.2f} and {secondNumber:.2f} is equal to {calculater(firstNumber, secondNumber, operation):.2f}.')