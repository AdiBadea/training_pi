#SURSA: https://www.w3resource.com/python-exercises/class-exercises/

#1. Write a Python class to convert an integer to a roman numeral.

class IntToRomanNumeral:
    def __init__(self, numbers):
        for self.number in numbers:
            number = self.number

            if  number < 10:
                if number = 9:
                    convertedNumber = "IX"
                elif number = 8:
                    convertedNumber = "VIII"
                elif number = 7:
                    convertedNumber = "VII"
                elif number = 6:
                    convertedNumber = "VI"
                elif number = 5:
                    convertedNumber = "V"
                elif number = 4:
                    convertedNumber = "IV"
                elif number = 3:
                    convertedNumber = "III"
                elif number = 2:
                    convertedNumber = "II"
                elif number = 1:
                    convertedNumber = "I"
                elif number = 0:
                    convertedNumber = "III"

            print("Input number:", number)
            print("Roman number:", convertedNumber)

numbers = [1,2,3]

IntToRomanNumeral(numbers)
print(76%10)
#------------------------------------------------------------------------------------