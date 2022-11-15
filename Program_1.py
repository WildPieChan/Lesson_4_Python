from math import pi

def InputNumber(inputText):
    ok = False
    while not ok:
        try:
            number = int(input(f"{inputText}"))
            ok = True
        except ValueError:
            print("Erroe. Only integer numbers. Try again...")
    return number

def AccuracyMeaning(number):
    result = '0.'
    for i in range(number):
        if i != number - 1:
            result += '0'
        else:
            result += '1'
    return result


d =  InputNumber("Enter an accuracy for number Pi: ")
if d != 0:
    accuracy = float(AccuracyMeaning(d))
else:
    accuracy = d

if accuracy == 0:
    print(f'Pi with accuracy {accuracy}: {round(pi, d):.0f}')
else:
    print(f'Pi with accuracy {accuracy}: {round(pi, d)}')