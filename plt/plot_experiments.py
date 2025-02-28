# AUTHOR: Sven Schrodt
# SINCE: 2025-02-26
import matplotlib.pyplot as plt
import random

for x in range(640):
    y = random.randrange(55)
    plt.plot(x, y, '.', markersize=.1, color='blue')
plt.show()