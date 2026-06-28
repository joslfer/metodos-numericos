"""
Descenso de Gradiente

Recursos:
- https://youtu.be/IHZwWFHWa-w?si=xFcdVV36dmh4xRxl
- https://youtu.be/FeEUeX0NlDg?si=KVZCC9VCbThhx0VL

Tenemos una función L(θ) que mide qué tan mal se ajusta el modelo a los datos.

Como el gradiente ∇L(θ) indica en qué dirección sube más rápido la función,
es decir, en qué dirección se ajusta peor, queremos movernos en la dirección
contraria para encontrar parámetros mejores. Nuestros nuevos parámetros serán:

  θ ← θ - α · ∇L(θ)

La función de coste es el error cuadrático medio:

  L(a, b) = (1/N) Σ (yᵢ - (a·xᵢ + b))²

El gradiente se calcula con las derivadas parciales:

  ∂L/∂a = -(2/N) Σ (yᵢ - (a·xᵢ + b)) · xᵢ
  ∂L/∂b = -(2/N) Σ (yᵢ - (a·xᵢ + b))
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Generamos valores aleatorios
np.random.seed(67)

x = np.linspace(0, 10, 100)
y = 3*x + 2 + np.random.randn(100) * 1.5

plt.xlabel("$x$")
plt.ylabel("$y$", rotation=0)
plt.scatter(x, y, s=10)

"""
El proceso de optimización:

  θₙ = θₙ₋₁ - α ∇L(θₙ₋₁)

Queremos optimizar a (pendiente) y b (corte con el eje y):

  θ = [a, b]ᵀ

Las ecuaciones de actualización quedan:

  aₙ = aₙ₋₁ - α · (2/N) · xᵀ((a·x + b) - y)
  bₙ = bₙ₋₁ - α · (2/N) · Σ((a·x + b) - y)
"""

a = 0
b = 0
n = 1000
N = len(x)
alpha = 0.01

L = []

a_record = []
b_record = []
for paso in range(n):
    l = (1/N) * np.sum((y - (a*x + b))**2)
    L.append(l)
    a_record.append(a)
    b_record.append(b) 
    grad_a = (2/N) * x @ ((a*x + b) - y)
    grad_b = (2/N) * np.sum((a*x + b) - y)
    a = a - alpha * grad_a
    b = b - alpha * grad_b


print(a)
print(b)

fig, ax = plt.subplots(1, 2)

ax[0].set_title("Ajuste lineal")
ax[0].plot(x, a*x + b, color="red")
ax[0].scatter(x, y)

ax[1].set_title("Función de pérdida")
ax[1].set_xlabel("Iteración")
ax[1].set_ylabel("L")
ax[1].plot(L)
ax[1].set_yscale("log")

"""
Superficie de coste J(a, b)
Para cada par (a, b) de la rejilla calculamos el coste.
"""

a_vals = np.linspace(0, 4, 100)
b_vals = np.linspace(0, 4, 100)

A, B = np.meshgrid(a_vals, b_vals)

J = np.zeros([len(a_vals), len(b_vals)])

for i in range(len(a_vals)):
    for j in range(len(b_vals)):
        J[i, j] = (1/N) * np.sum((y - (A[i, j]*x + B[i, j]))**2)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(A, B, J, alpha = 0.5)
ax.set_xlabel("$a$")
ax.set_ylabel("$b$")
ax.set_zlabel("$J(a,b)$")


line, = ax.plot([],[],[], color = "orange", linewidth =2, zorder=5)

L_elevated = [l + 2 for l in L]
def update(frame):
    line.set_data(a_record[:frame], b_record[:frame])
    line.set_3d_properties(L_elevated[:frame])
    return line,



ani = FuncAnimation(fig,update, frames= len(a_record), interval = 200)

#ani.save("descenso.gif", writer="pillow")

plt.show()

