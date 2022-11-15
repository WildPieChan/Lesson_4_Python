import random

def CreateRandomArray():
    length = random.randint(5, 11)
    array = []
    for i in range(length):
        number = random.randint(1, 11)
        array.append(number)
    return array

def SortedArray(array):
    i = 0
    while i < len(array) - 2:
        if array[i] == array[i + 1]:
            array.remove(array[i])
        else:
            i += 1
    return array

# sortedArray = []
# [sortedArray.append(i) for i in array if i not in sortedArray]
# print(sortedArray)

array = CreateRandomArray()
print(array)
array = sorted(array)
array = SortedArray(array)
print(array)
