import numpy as np 

def rk4(f, y0, t0, h, n):
    t = np.zeros(n+1) # n+1 puntos porque incluye el t0 (n es el número de pasos que se dan)
    y = np.zeros((n+1,len(y0)))
    y[0] = np.atleast_1d(np.array(y0, dtype = float))
    t[0] = t0
    for paso in range(n):

        k1 = f(t[paso],y[paso])
        k2 = f(t[paso] + (h/2), y[paso] + (k1 * h/2))
        k3 = f(t[paso] + (h/2), y[paso] + (k2 * h/2))
        k4 = f(t[paso] + h, y[paso] + (k3 * h))
        
        y[paso+1] = y[paso] + h * ((k1+2*k2+2*k3+k4)/6)
        t[paso+1] = t[paso] + h
    return t , y 

