''' Ejercicio 6:
     Un estacionamiento requiere determinar el cobro que debe aplicar a las personas que lo utilizan.
     Considere que el cobro es con base en las horas que lo disponen y que las fracciones de hora se toman
     como completas. Cree un programa que realice el cobro del estacionamiento.
                                                          --- '''
#Ingresar lo que cobran por hora.
print ("Ingrese el precio del estacionamiento por hora:")
precio = int(input())

print(' ')

#Ingresar las hora que uso el estacionamiento.
print ("Ingrese las horas que estuvo en el estacionamiento:")
horas = float(input())

#El redondeo aumenta la cifra si es mayor a 5, si es 5 o menos se queda igual.
total = precio * round(horas)

print(' ')

# Total a pagar por el usuario.
print("El total a pagar por las", round(horas), "horas que estuvo en el estacionamiento es de:", total,"pesos")
