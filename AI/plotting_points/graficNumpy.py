import matplotlib.pyplot as plt
import numpy as np

# y = x + 0
# xCoords = [0, 1, 2, 3, 4]
# yCoords = [0, 1, 2, 3, 4]

# y = x + 1
                    #start stop step
xCoords = np.arange(0, 11, 1)
yCoords = xCoords * 1 + 1

print(xCoords, yCoords)

#yCoords = np.array(xCoords) + 1
# dar xCoords este deja formatat cum trebuie

xCoords2 = np.arange(0, 11, 1)
yCoords2 = (xCoords * 0.5) + 1


print(xCoords2, yCoords2)

plt.plot(xCoords, yCoords)
plt.plot(xCoords2, yCoords2, color="red")

plt.show()