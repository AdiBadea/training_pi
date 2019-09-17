
# for pin in pins:
#     print(pin)

class activatePins:
    def __init__(self, pins):
        self.pins = pins
        self.activationFunction(pins)
    
    def activationFunction(self, pins):
        for self.pin in self.pins:
            print(self.pin)

pinsArray = [1, 6]
    
activatePins(pinsArray)