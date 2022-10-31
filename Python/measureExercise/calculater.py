def calculater (firstNumber:float, secondNumber:float, operation:str):
    """This function will calculate two values ​​in the same order (firstNumber and secondNumber) considering the operations of addition, subtraction, multiplication and division. 
    
    Arguments:
        firstNumber (float): First number to be used for calculation.
        secondNumber (float): Second number to be used for calculation.
        operation (str): Describe which operation you want to use in this operation.
    """

    match operation:
        case('+'):
            result = firstNumber + secondNumber
        case('-'):
            result = firstNumber - secondNumber
        case('*'):
            result = firstNumber * secondNumber
        case('/'):
            result = firstNumber / secondNumber

    return result