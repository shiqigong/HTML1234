import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 1000)
y = np.exp(x)

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("exp(x)")
plt.title("Graph of the Exponential Function")
plt.grid()
plt.show()
