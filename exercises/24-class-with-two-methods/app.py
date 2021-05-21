class Sphgetti(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input("Input your string here to convert to upper case : ")

    def printString(self):
        print(self.s.upper())

strObj = Sphgetti()
strObj.getString()
strObj.printString()