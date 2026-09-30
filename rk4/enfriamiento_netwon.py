import numpy as np
import matplotlib.pyplot as plt
from rk4 import rk4



t = np.linspace(0,120,1000)
C = 90
S_0= 20
k = 0.05
T = S_0 + C*np.exp(-k*t)


def enfriamiento(t,y):
    T = y[0]
    return np.array([-k*(T-S_0)])


t_rk, T_rk = rk4(enfriamiento, [C+S_0], 0, 0.5, 240)

plt.plot(t,T, color = "red",label= "Solución analítica")
plt.plot(t_rk, T_rk[:,0], color = "blue", label = "Solución con RK4")
plt.grid()

plt.ylim(0,120)
plt.xlim(0,120)
plt.title("Ecuación del enfriamiento de Newton")
plt.text(85,100, "C = 90, S_0 = 20", bbox=dict(boxstyle="round", facecolor="white", alpha=0.8)) # bbox significa bounding box
plt.legend()
plt.show()

