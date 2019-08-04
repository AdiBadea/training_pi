class TestClass:
    def __repr__(self):

        return self.functieTest()

    def functieTest(self):
        data = "Banane"
        return data

print(TestClass())