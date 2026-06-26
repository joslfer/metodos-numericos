import numpy as np 
import matplotlib.pyplot as plt
from rk4 import rk4

#ecuacion del oscilador: x'' + gamma x' + w^2 x = 0 
w = 1 #frecuencia
gamma = 0.2 #amortiguamiento

h = 0.1
n = 200
def f(t,y):
    x, v = y
    return np.array([v, -gamma*v - w**2*x])


y0 = np.array([1,0])
t, y = rk4(f, y0, t0=0, h = h, n = n)


# w damped = sqrt(w^2-(gamma/2)^2)
wd = np.sqrt(w**2-(gamma/2)**2)
# solución exacta x = e^((-gamma/2)*t)*(cos(wdt)+ (gamma/2*wd) *sin(wd*t) )
y_exacto = np.exp((-gamma/2)*t)*(np.cos(wd*t)+(gamma/(2*wd))*np.sin(wd*t))

error_absoluto = (y[:,0] - y_exacto)
# solución exacta de la velocidad (derivando la sol. exacta de la posición)
# v(t) = -w^2/wd *e^-(gammma/2)*t*sin(wd*t)
v_exacto = -(w**2/wd)*np.exp((-gamma/2)*t)*np.sin(wd*t)

mapa = [["comparacion","comparacion"],["fases", "error"]]
fig, ax = plt.subplot_mosaic(mapa, figsize=(12,6))

ax["comparacion"].plot(t,y[:,0], color = "red",marker=".",linestyle ="None",markersize =4, label ="RK4")
ax["comparacion"].plot(t,y_exacto, color = "blue",linewidth=3,alpha = 0.5, label ="Solución analítica")
ax["comparacion"].set_xlabel("Tiempo (t)")
ax["comparacion"].set_ylabel("Posición (x)")
ax["comparacion"].set_title("Comparación")
ax["comparacion"].grid()
ax["comparacion"].legend()

ax["fases"].plot(y[:,0],y[:,1], color = "red", marker=".",linestyle = "None", markersize = 4, label = "RK4")
ax["fases"].plot(y_exacto, v_exacto, color="blue", linewidth = 3, alpha = 0.5, label = "Solución analítica")
ax['fases'].set_xlabel("Posición (x)")
ax['fases'].set_ylabel("Velocidad (v)")
ax['fases'].legend()
ax['fases'].set_title("Espacio de Fases")
ax['fases'].grid(True)

ax['error'].plot(t, error_absoluto, color="red")
ax['error'].set_xlabel("Tiempo (t)")
ax['error'].set_ylabel("|x_aproximado - x_exact|")
ax['error'].set_title(f"Error Absoluto (h={h})")
ax['error'].grid(True)

fig.suptitle("RK4 del Oscilador Armónico", y = 0.96)
fig.tight_layout(pad = 1.3, rect=[0, 0, 1, 0.98])
plt.show()