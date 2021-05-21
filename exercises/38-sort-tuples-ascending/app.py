from operator import itemgetter, attrgetter

data = input("Input your data separated by comma : ")
dataList = [tuple(l.split(',')) for l in data.split(' ') if l]

print(sorted(dataList,key=itemgetter(0,1,2)))