''' Ejercicio 5:
    Una empresa que contrata personal requiere determinar la edad de cada una de las personas que
    solicitan trabajo, pero cuando se les realiza la entrevista solo se les pregunta el año en que nacieron.
    También se requiere el promedio de edad de las personas contratadas.
                                         --- '''

actual = 2021
personas = 0

# Cantidad de trabajores contratados.
print( "Ingrese la cantidad de trabajadores incorporados recientemente ")
n = int(input())

print(' ')

# Calculo de sus edades actuales, según su año de nacimiento.
while personas < n:
    print(" Año de nacimiento de los trabajadores: ")
    nacimiento = int(input())
    edad = actual - nacimiento
    print( " Este trabajador nació en el año ", nacimiento, " y tiene ", edad," años aproximadamente ")
    print (' ')
    edad += edad
    personas = personas + 1

promedio = edad / n

# El promedio de edades se aproxima.
print(" El promedio de las edades de las personas contratadas es de: ", round(promedio)," años ")
    
    

        


    
    


