#“An outbreak anywhere is a risk everywhere.”
# — Tedros Adhanom Ghebreyesus

import numpy as np 
import matplotlib.pyplot as plt
from rk4 import rk4

a = 0.4 #0.4 sugerido
b = 0.1
y0 = np.array([9999,1,0]) 
t0 = 0 

h = 0.01
n = 20000
N = y0[0]+y0[1]

def f(t,y):
    S, I, R = y
    return np.array([-a*((S*I))/N,a*((S*I)/N)-b*I,b*I])

t, y = rk4(f,y0,t0,h,n)

S = y[:,0]
I = y[:,1]
R = y[:,2]

R0_vals = [0.8,1.5,2.5,4.0]

s_vals = np.linspace(0,N,20)
i_vals = np.linspace(0,N,20)
SS, II = np.meshgrid(s_vals, i_vals)

dS = -a*SS*II/N
dI = a*SS*II/N-b*II

magnitud = np.sqrt(dS**2+dI**2)
s_fill = np.linspace(0, N, 100)


mapa = [["ejemplo","fases"],["comparacion","fases"]]
fig, ax = plt.subplot_mosaic(mapa, figsize = (12,6))


ax["ejemplo"].plot(t,S, label = "Susceptibles", color = "blue")
ax["ejemplo"].plot(t,I, label = "Infectados", color = "red")
ax["ejemplo"].plot(t,R, label = "Recuperados", color = "orange")
ax["ejemplo"].set_ylabel("Número de personas")
ax["ejemplo"].set_xlabel("Tiempo")
ax["ejemplo"].grid()

ax["fases"].quiver(SS,II,dS/magnitud,dI/magnitud, magnitud, cmap = "plasma")
ax["fases"].plot(S,I, color = "purple",linewidth = 3)
ax["fases"].fill_between(s_fill, N - s_fill, N, alpha=0.3, color="gray", label="Zona no física")
ax["fases"].set_ylabel("I (personas infectadas)")
ax["fases"].set_xlabel("S (personas susceptibles)")
ax["fases"].grid()

cmap = plt.cm.magma
colores = [cmap(i) for i in np.linspace(0,0.85,len(R0_vals))]

for R0, color in zip(R0_vals, colores):
    a = R0*b
    
    def f_bucle(t,y):
        S, I, R = y
        return np.array([-a*S*I/N, a*S*I/N - b*I, b*I])

    t,y = rk4(f_bucle,y0,t0,h,n)

    I = y[:,1]
    ax["comparacion"].plot(t,I,label=f"R0={R0}",color = color)

ax["comparacion"].set_xlabel("Tiempo")
ax["comparacion"].set_ylabel("Número de personas")
ax["comparacion"].set_title(f"Comparación de R0 (b = {b})")

fig.suptitle("Modelo SIR de una pandemia",)
fig.tight_layout(pad = 1.3, rect=[0, 0, 1, 0.98])
plt.legend()
plt.grid()
plt.show()