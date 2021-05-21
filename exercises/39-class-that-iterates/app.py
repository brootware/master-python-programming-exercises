# class genClass:
#     def __init__(self, num):
#         self.num = num

def generator(n):
    count = 0
    while count < n:
        j = count
        count += 1
        if j % 7 == 0:
            yield j
    
    # def displayCount(self):
    #     print(self.generator)

# obj = genClass(100)

# genClass.displayCount()

for item in generator(100):
    print(item)