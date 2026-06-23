# Método RK4 para solucionar ecuacinoes diferenciales

import numpy as np 
import matplotlib.pyplot as plt

# Sea la ecuación diferencial: 

def f(t,y):
    return y
# (esta ecuación va a cambiar para cada problema)
# ahora es y(t) = y0 e^t


y0 = 1 
t0 = 0 
h = 0.05 
n = 100

# Método general 

def rk4(f, y0, t0, h, n):
    y_actual = y0
    t_actual = t0
    y = []
    t = []   
    for paso in range(n):

        k1 = f(t_actual,y_actual)
        k2 = f(t_actual + (h/2), y_actual + (k1 * h/2))
        k3 = f(t_actual + (h/2), y_actual + (k2 * h/2))
        k4 = f(t_actual + h, y_actual + (k3 * h))

        k =(k1+2*k2+2*k3+k4)/6
        
        y_actual = y_actual + h * k
        t_actual = t_actual + h

        y.append(y_actual)
        t.append(t_actual)
    return t , y 

t, y = rk4(f,y0,t0,h,n)

t = np.array(t)
y = np.array(y)


y_exacto = y0 * np.exp(t)

fig, ax = plt.subplots(1, 2)

ax[0].plot(t, y, color='black')
ax[0].plot(t, y_exacto, color='red')
ax[0].set_title('RK4')
ax[0].grid()

error = np.abs(y - y_exacto)
ax[1].plot(t, error)
ax[1].set_title('Error RK4')
ax[1].grid()


plt.show()
