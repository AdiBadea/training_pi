# print("1 - Verde | 2 - Galben | 3 - Rosu")

# print("Pentru cate secunde ?")
# secundeAprins = input()

# aprinsBec = input()
# print("Aprindem " + aprinsBec)
# print("Pentru ", secundeAprins, "secunde")

parametrii = []

class AprindeBec:

    def puneIntrebari():
        print("Ce bec doresti sa aprinzi?")
        print("1 - Verde | 2 - Galben | 3 - Rosu")
        becDeAprins = input()
        print("Aprindem becul ", str(becDeAprins))

        return becDeAprins

    print(puneIntrebari())


AprindeBec()




    

