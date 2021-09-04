''' Ejercicio 9 :
    Se requiere obtener la distancia entre dos puntos en el plano cartesiano, tal y como se muestra en la
    figura siguiente.

    Para resolver este problema es necesario conocer las coordenadas de cada punto (X, Y), y con esto
    poder obtener el cateto de abscisas (X 1 y X 2 ) y el de ordenadas (Y 1 e Y 2 ), y mediante estos valores
    obtener la distancia entre P 1 y P 2 , utilizando el teorema de Pitágoras.
                                             --- '''

# Asignar valor para el punto X 1.
print(" Ingrese un valor para el punto X 1 : ")
x_1 = int(input())

print(' ')

# Asignar valor para el punto X 2.
print(" Ingrese un valor para el punto X 2 : ")
x_2 = int(input())

print(' ')

# Asignar valor para el punto Y 1.
print(" Ingrese un valor para el punto Y 1 : ")
y_1 = int(input())

print(' ')

# Asignar valor para el punto Y 2.
print(" Ingrese un valor para el punto Y 2 : ")
y_2 = int(input())

# Coordenadas mostradas en pantalla.
print(" Las coordenadas de las abscisas (eje X) son : ", (x_1,x_2))
print(" Las coordenas de las ordenadas  (eje Y) son : ", (y_1,y_2))

# Calculo de la distancia entre 2 puntos.
distancia = ((x_2 - x_1)**2 + (y_2 - y_1)**2)**0.5

print(' ')

# La distancia entre los puntos.
print(" La distancia que hay entre estos 2 puntos en el plano cartesiano es de : ", distancia)
