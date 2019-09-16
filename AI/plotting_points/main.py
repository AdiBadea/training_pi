import matplotlib.pyplot as plt
import numpy as np

from os import system, name 
# system('cls') 

# Cum pun un punct
# plt.plot([x], [y], marker='o', markersize=3, color="red")

points = [
    #x   y
    [3, 1],
    [1, 3]
]

for point in points:

  i = 0
  while i < len(point):
    plt.plot([point[0]], [point[1]], marker='o', markersize=3, color="red")
    i += 1

def plotDivider(xCoords, yCoords, color):
  plt.plot(xCoords, yCoords, color=color)

# -------------------------------------------------

#DEFAULT | CONTROL | y = x
xControlCoords = np.arange(0, 11, 1)
yControlCoords = xControlCoords 
#            y = x

#TEST 1 | y = x + 1
xCoordsTest1 = xControlCoords
b1 = 1
yCoordsTest1 = xCoordsTest1 + b1
#          y = x            + 1

#TEST 2 | y = x * 2 + 1
xCoordsTest2 = xControlCoords
w2 = 2
b2 = 1
yCoordsTest2 = (xCoordsTest2 * w2) + b2

#TEST 3 | y = x * 2 + 2
xCoordsTest3 = xControlCoords
w3 = 3
b3 = 1
yCoordsTest3 = (xCoordsTest3 * w3) + b3

# -------------------------------------------------
# NOTITE:

# xControlCoords = np.arange(0, 11, 1) #incepe din punctul 0, trece prin 10 si o i-a din 1 in 1

# yCoords = (xCoords * 0.5) + 1 # y = x + 1
#! weight modifica panta, weight = panta
#! bias translateaza linia stanga dreapta

#! Liniile nu exista cu adevarat, ele sunt doar puncte unite, iar un punct are o cordonata X si Y.
#! In python feeduiesti un array cu coordonate ptr X si un alt array pentru coordonate ptr Y
#Exemplu: cordX = [x1, x2], cordY = [y1, y2] 

  # -------------------------------------------------

#Control
plotDivider(xControlCoords, yControlCoords, "blue")

#TEST 1
plotDivider(xCoordsTest1, yCoordsTest1, "red")

#TEST 2
plotDivider(xCoordsTest2, yCoordsTest2, "green")

#TEST 3
plotDivider(xCoordsTest3, yCoordsTest3, "yellow")

plt.xlabel('Axa X')
plt.ylabel('Axa Y')
plt.show()