class Person:
    def __init__(self, nume, varsta):
        self.nume = nume
        self.varsta = varsta

    def imbatrinire(self):
        self.varsta += 1

    def afisareDate(self):
        print(self.nume)
        print(self.varsta)

class Student(Person):
    def __init__(self, nume, varsta, anAbsolvire):
        super().__init__(nume, varsta)
        self.anAbsolvire = anAbsolvire

    def afisareDate(self):
        # print(self.nume)
        # print(self.varsta) 
        super().afisareDate()
        print(self.anAbsolvire)


study = Student("Gigel", 35, "2099")

study.afisareDate()

study.imbatrinire()

study.imbatrinire()

study.imbatrinire()

study.afisareDate()