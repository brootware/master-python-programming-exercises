import math
Input = input("Input : ").split(',')

listToSquare = [int(i) for i in Input]
squaredList = [pow(i,2) for i in listToSquare]
print(squaredList)