import random

def NumbersForEquation(quantity):
    array = [random.randint(0, 21) for i in range(quantity + 1)]
    return array

def EquationCreate(numbersArray):
    result = ''
    if len(numbersArray) < 1:
        result = 'x = 0'
    else:
        for i in range(len(numbersArray)):
            if i != len(numbersArray) - 1 and numbersArray[i] != 0 and i != len(numbersArray) - 2:
                result += f'{numbersArray[i]}x^{len(numbersArray) - i - 1}'
                if numbersArray[i + 1] != 0:
                    result += ' + '
            elif i == len(numbersArray) - 2 and numbersArray[i] != 0:
                result += f'{numbersArray[i]}x'
                if numbersArray[i + 1] != 0:
                    result += ' + '
            elif i == len(numbersArray) - 1 and numbersArray[i] != 0:
                result += f'{numbersArray[i]} = 0'
            elif i == len(numbersArray) - 1 and numbersArray[i] == 0:
                result += ' = 0'
    return result

def AnswerToFile(result):
    with open('file.txt', 'w') as data:
        data.write(result)

k = int(input("Enter the natural degree: k = "))
ratio = NumbersForEquation(k)
AnswerToFile(EquationCreate(ratio))
