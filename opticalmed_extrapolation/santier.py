import numpy as np

def stringToInt(string):
    return int(string)

print(stringToInt("3"))


arr = ["1", "2", "3"]

arr2 = map(stringToInt, arr)

print(list(arr2))