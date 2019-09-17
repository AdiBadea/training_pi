class ClasaMea:
    def __init__(self, text = "Nimic"):
        self.text = text
        print("In constructor:", text)
    
    def printHello(self):
        # print("In fucntia printHello:", text)
        print("Self.text in print hello", self.text)

x = ClasaMea(text = "ceva")

x.printHello()