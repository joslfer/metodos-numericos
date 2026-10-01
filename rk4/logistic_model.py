import numpy as np
import matplotlib.pyplot as plt
from rk4 import rk4



t = np.linspace(0,10,1000)
M = 100
r = 0.01
P0 = 1
P = (P0*M)/(P0+((M-P0)*np.exp(-r*M*t)))

def logistic(t,y):
    P = y[0]
    return np.array([r*(M-P)*P])

t_rk, P_rk = rk4(logistic, [1], 0, 0.5, 20)


plt.figure(figsize=(10,5))
plt.plot(t,P, color = "red",label= "Solución analítica")
plt.plot(t_rk, P_rk[:,0], color = "blue", label = "Solución con RK4")
plt.grid()

plt.title("Modelo Logísitico")
plt.text(7, 50, "P0 = 1, r = 0.01, M = 100\nrP0 sería la tasa de crecimiento \nsin límite de recursos. ")
plt.legend()

plt.savefig("images/logisticmodel.png",dpi = 200, bbox_inches = "tight")
plt.show()

