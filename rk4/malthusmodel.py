import numpy as np
import matplotlib.pyplot as plt
from rk4 import rk4



t = np.linspace(0,10,1000)
C = 1
k = 1
P = C*np.exp(k*t)


def malthus(t,y):
    P = y[0]
    return np.array([k*P])

t_rk, P_rk = rk4(malthus, [1], 0, 0.5, 20)


plt.figure(figsize=(10,5))
plt.plot(t,P, color = "red",label= "Solución analítica")
plt.plot(t_rk, P_rk[:,0], color = "blue", label = "Solución con RK4")
plt.grid()
plt.text(2,15000,"C = 1, k = 1, esto quiere decir \nque en el primer día aumenta \nal 270% la población")
plt.text(2,10000,"k indica el número de individuos \nque produce cada indiviudo por \nunidad de tiempo")

plt.title("Modelo de Malthus")
plt.legend()

plt.savefig("images/malthusmodel.png",dpi = 200, bbox_inches = "tight")
plt.show()

