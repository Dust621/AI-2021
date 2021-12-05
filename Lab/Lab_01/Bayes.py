import math
import matplotlib.pyplot as plt
import numpy as np
from numpy.core.defchararray import array

PHE = float(input("输入P(H|E):"))
PH = float(input("输入P(H):"))
PH_E = float(input("输入P(H|_E):"))
PE = float(input("输入P(E):"))

PES = np.linspace(0, 1, 500)
PHS = []
for x in PES:
    if ((x >= 0) & (x < PE)):
        PHS.append(PH_E + (PH - PH_E) / PE * x)
    elif((x >= PE) & (x <= 1)):
        PHS.append(PH + (PHE - PH) / (1 - PE) * (x - PE))
        
plt.plot(PES, PHS)
plt.show()
