class Calculation:
    def __init__(self, inputNumber = 0):
        self.inputNumber = inputNumber
    
    def add1(self):
        self.inputNumber = self.inputNumber + 1
        return self.inputNumber
    
    def addNumber(self, number):
        result = self.inputNumber + number
        return result

myNumber = Calculation(5)

test1 =   myNumber.add1()
myNumber = Calculation(test1)
test1 = myNumber.add1()
print(test1)


test2 = myNumber.addNumber(2)
print(test2)