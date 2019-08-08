class Person:
    def __init__(self, name, age):
      self.name = name
      self.age = age

    def echivPers(self, person):
        if self.name == person.name and self.age == person.age:
            return True
        else:
            return False

    def printName(self):
        print(self.age, self.name)

    def __str__(self):
        return self.name + " " + str(self.age)
  
p1 = Person("John", 36)
p2 = Person("Adrian", 23)
p3 = Person("John", 36)

# p1.printName()
print(p1)
print(p2)
print(p1.echivPers(p2))
  
# print(p1.name)
# print(p1.age)