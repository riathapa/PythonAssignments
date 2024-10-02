def calculateAverage(list1):
    lowerNumber = list1[0]
    higherNumber = list1[0]
    for i in range(len(list1)):
       if list1[i] < lowerNumber:
           lowerNumber = list1[i]

    for i in range(len(list1)):
       if(list1[i] > higherNumber):
           higherNumber = list1[i]

    print("Higher Number :: ", higherNumber)
    print("Lower Number :: ", lowerNumber)

    print("Average :: ", (higherNumber + lowerNumber) / 2)

list1 = [21, 43, 554, 76, 68, 43, 0]
calculateAverage(list1)