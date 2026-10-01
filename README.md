# metodos-numericos

Implementar métodos que aproximan las soluciones a diversos problemas en Python. He ido añadiendo varios modelos que he visto en la asignatura de Ecuaciones Diferenciales.

## RK4

Definiendo la función RK4 se resuelve:

- El oscilador armónico amortiguado, partiendo de su ecuación. 

![Gráficos Oscilador Armónico](images/oscilador.png)

- Un modelo de pandemia SIR con el número de Susceptibles, Infectados y Recuperados. También se comparan distintos R0, parámetro importante para predecir el contagio de un virus.

![Simulación SIR](images/sir.png)


![Modelo de Malthus](images/malthusmodel.png)

- La ecuación del modelo de malthus es: dP/dt = kP. El crecimiento de la población es proporcional a k, la diferencia entre la tasa de nacimientos y la de muertes. Si k es positivo entonces la población explota. Este modelo de población no tiene en cuenta recursos, por eso no es realista. La solución es una ecuación exponencial P(t) = C_0 * e^(kt)

![Enfriamiento de Newton](images/enfriamiento.png)

- La ecuación diferencial dT/dt = -k(T-S) es un decaimiento exponencial. Tiene como solución analítica: T(t) = S_0 + C*e^(-kt). 
Podría modelar la temperatura de un cazo con agua muy caliente en una habitación a temperatura ambiente. 


## Descenso de gradiente

Aplicar el descenso de gradiente de machine learning para encontrar parámetros de un ajuste lineal y = a*x+b.


![Descenso de gradiente](images/descenso.gif)


