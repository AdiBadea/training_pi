import matplotlib.pyplot as plt
from os import system, name 

system('cls') 

print("-------------------------------------------------------------")

# Cum pun un punct
# plt.plot([x], [y], marker='o', markersize=3, color="red")

points = [
    #x    y
    [3.1, 1.2],
    [1, 3],
    [3, 1],
    [2.9, 0.8],
    [1.4, 2.7]
]

for point in points:

  i = 0
  while i < len(point):
    plt.plot([point[0]], [point[1]], marker='o', markersize=3, color="red")
    i += 1

plt.xlabel('Axa X')
plt.ylabel('Axa Y')

plt.show()