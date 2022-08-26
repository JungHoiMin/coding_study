import numpy as np

Dean = np.array([3, 3, 7, 5])
Sam = np.array([2, 4, 0, 10])

Req = np.array([2, 10, 5, 10])

print(Dean[Dean+Sam >= Req])