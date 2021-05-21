X = input("Input : ")
dimensions = [int(x) for x in X.split(',')]
row = dimensions[0]
print(row)
col = dimensions[1]
print(col)

genList = [[0 for c in range(col)] for r in range(row)]
# print(genList)

for i in range(row):
    for j in range(col):
        genList[i][j] = i*j

print(genList)