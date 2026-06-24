# Método RK4 para solucionar ecuacinoes diferenciales

import numpy as np 
import matplotlib.pyplot as plt


def f(t,y):
    return np.cos(t)

y0 = 0
t0 = 0
h = 0.5
n = 100


def rk4(f, y0, t0, h, n):
    t = np.zeros(n+1)
    y = np.zeros(n+1)
    y[0] = y0
    t[0] = t0
    for paso in range(n):

        k1 = f(t[paso],y[paso])
        k2 = f(t[paso] + (h/2), y[paso] + (k1 * h/2))
        k3 = f(t[paso] + (h/2), y[paso] + (k2 * h/2))
        k4 = f(t[paso] + h, y[paso] + (k3 * h))

        k =(k1+2*k2+2*k3+k4)/6
        
        y[paso+1] = y[paso] + h * k
        t[paso+1] = t[paso] + h
    return t , y 

t, y = rk4(f,y0,t0,h,n)
t_exacto = np.linspace(t[0], t[-1], 1000)

plt.figure()


plt.plot(t_exacto, np.sin(t_exacto), label='Solución Exacta', color='red')
plt.plot(t, y, label='Aproximación RK4', color='blue',linestyle='--')

plt.grid(True)
plt.legend()
plt.show()