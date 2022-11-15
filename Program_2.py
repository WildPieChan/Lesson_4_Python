def InputNumber(inputText):
    ok = False
    while not ok:
        try:
            number = int(input(f"{inputText}"))
            ok = True
        except ValueError:
            print("Error. Only integer numbers. Try again...")
    return number

def PrimeFactors(number):
    multipliers = []
    divider = 2
    ok = False
    while number != 1:
        if number % divider == 0:
            multipliers.append(divider)
            number //= divider
            ok = True
            divider = 2
        else:
            divider += 1
    return multipliers


n = InputNumber("Enter any integer number: ")
result = PrimeFactors(n)
print(result)

