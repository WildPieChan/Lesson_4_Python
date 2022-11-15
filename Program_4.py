import random

def NumbersForEquation(quantity):
    array = [random.randint(0, 21) for i in range(quantity + 1)]
    return array
    
def EquationCreate(sp):
    lst= sp[::-1]
    wr = ''
    if len(lst) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                wr += f'{lst[i]}x^{len(lst)-i-1}'
                if lst[i+1] != 0:
                    wr += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                wr += f'{lst[i]}x'
                if lst[i+1] != 0:
                    wr += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                wr += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                wr += ' = 0'
    return wr

def AnswerToFile(st):
    with open('file.txt', 'w') as data:
        data.write(st)

k = int(input("Enter the natural degree: k = "))
ratio = NumbersForEquation(k)
AnswerToFile(EquationCreate(ratio))