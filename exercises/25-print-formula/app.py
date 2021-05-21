import math

inputList = input("Enter your numbers separated by numbers : ").split(',')
outputList = []

for D in inputList:
    D = int(D)
    Q = round(math.sqrt((2 * 50 * D)/30))
    outputList.append(Q)

print(outputList)