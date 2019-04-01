# List Functions

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
stack = [3, 4, 5, 8, 13, 17, 35, 42]


def largestElement(listInput):
    try:
        return max(listInput, key=len)
    except:
        return max(listInput)


def reverseList(listInput):
    listInput.reverse()
    print(listInput)


def contains(element, inputList):
    if element in inputList:
        return True
    return False


def oddPositionElements(listInput):
    oddElements = []
    index = 1
    while index < len(listInput):
        oddElements.append(listInput[index])
        index += 2
    return oddElements


def totalList(listInput):
    runningTotal = []

    totalInt = 0
    totalString = ""

    for element in listInput:
        if isinstance(element, str):
            totalString += element
            runningTotal.append(totalString)
        else:
            totalInt += element
            runningTotal.append(totalInt)

    return runningTotal


print("Fruit list: " + fruits.__str__())
print("Integer list: " + stack.__str__())

print("\nThe largest fruit is %s." % largestElement(fruits))
print("The largest integer is %d." % largestElement(stack))


print("\nReversed fruit list: ")
reverseList(fruits)
print("Reversed integer list:")
reverseList(stack)


print("\nFruit list contains apple: %r" % contains('apple', fruits))
print("Fruit list contains bacon: %r" % contains('bacon', fruits))
print("Integer list contains 17: %r" % contains(17, stack))
print("Integer list contains 7: %r" % contains(7, stack))

print("\nOdd positioned fruits: " + oddPositionElements(fruits).__str__())
print("Odd positioned integers: " + oddPositionElements(stack).__str__())


print("\nRunning total of fruits: " + totalList(fruits).__str__())
print("Running total of integers: " + totalList(stack).__str__())