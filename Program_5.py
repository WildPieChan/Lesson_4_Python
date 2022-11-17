from itertools import *
import os
os.system("cls")

file1 = 'file_1.txt'
file2 = 'file_2.txt'

def ReadPolinomial(file): 
    with open(str(file), 'r') as data:
        polinome = data.read()
    return polinome

def GetPolynomial(k, ratios):
    var = ['*x^'] * (k - 1) + ['*x']
    polynomial = [[a, b, c] for a, b, c in zip_longest(
        ratios, var, range(k, 1, -1), fillvalue = '') if a != 0]
    for x in polynomial:
        x.append(' + ')
    polynomial = list(chain(*polynomial))
    polynomial[-1] = ' = 0'
    return "".join(map(str, polynomial)).replace(' 1*x', ' x')

def ConvertPolinomial(polinome):
    polinome.replace('= 0', '')
    polinome = polinome.split(' + ')
    polinome = [i[0] for i in polinome]
    for i in range(len(polinome)):
        if polinome[i] == 'x':
            polinome[i] = '1'
    polinome = polinome[::-1]
    return polinome

firstPolinomial = ReadPolinomial(file1)
secondPolinomial = ReadPolinomial(file2)
print('Two polinomials:')
print(firstPolinomial)
print(secondPolinomial, '\n')
ConvertPolinomial(firstPolinomial)
ConvertPolinomial(secondPolinomial)
firstPolinomialCoef = list(map(int, ConvertPolinomial(firstPolinomial)))
secondPolinomialCoef = list(map(int, ConvertPolinomial(secondPolinomial)))
sumCoef = list(map(sum, zip_longest(firstPolinomialCoef, secondPolinomialCoef, fillvalue = 0)))
sumCoef = sumCoef[::-1]
sumOfPolinomials = GetPolynomial(len(sumCoef)-1, sumCoef)
print('The sum of two polinomials:\n', sumOfPolinomials)
with open('file_3.txt', 'w') as file_sum:
    file_sum.writelines(sumOfPolinomials)