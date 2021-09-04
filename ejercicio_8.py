''' Ejercicio 8:
    Se requiere obtener el área de la figura en la forma A de la siguiente imagen. Para resolver este problema
    se puede partir de que está formada por tres figuras: dos triángulos rectángulos, con H como hipotenusa
    y R como uno de los catetos, que también es el radio de la otra figura, una semicircunferencia que forma
    la parte circular (ver forma B).

    Por lo tanto, para poder resolver el problema, se tiene que calcular el cateto faltante, que es la altura
    del triángulo, con ésta se puede calcular el área del triángulo, y para obtener el área total triangular
    se multiplicará por dos. Por otro lado, para calcular el área de la parte circular, se calcula el área de
    la circunferencia y luego se divide entre dos, ya que representa solo la mitad del cı́rculo.
                                                        --- '''

# Asignar un valor para H.
print(" Ingrese un valor para H : ")
h = int(input())

print(' ')

# Asignar un valor para R.
print(" Ingrese un valor para R : ")
r = int(input())

print(' ')

# Cálculos para saber las áreas.
a = ( h**2 - r**2 )**0.5
area_1 = ((r * a) / 2) * 2
area_2 = (3.14 * r**2) / 2

# El área total de la figura 
print (" El área total de la figura es : ", area_1 + area_2)

