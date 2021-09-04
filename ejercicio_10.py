''' Ejercicio 10:
     Una empresa constructora vende terrenos con la forma A de la figura. Se requiere crear un programa
     para obtener el área respectiva de un terreno de medidas de cualquier valor.
    
     Para resolver este problema se debe identificar que la forma A está compuesta por dos figuras: un
     triángulo de base B y de altura (A - C); y por otro lado, un rectángulo que tiene base B y altura C y
     la suma de ambas áreas es el resultado final.
                                                       ---'''

# Asignar un valor para A.
print(" Ingrese un valor para asignar los metros de A : ")
a = int(input())

print(' ')

# Asignar un valor para B.
print(" Ingrese un valor para asignar los metros de B : ")
b = int(input())

print(' ')

# Asignar un valor para C.
print(" Ingrese un valor para asignar los metros de C : ")
c = int(input())

print(' ')

# Calculos para sacar el área del terreno.
a = a - c
area_1 = (a * b) / 2
area_2 = b * c

# El área total del terreno.
print(" El área total del terreno con la forma A es de : ", area_1 + area_2, " metros cuadrados")