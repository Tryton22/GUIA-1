''' Ejercicio 4:
    Se requiere un programa para determinar cuánto ahorrará una persona en un año, si al final de cada
    mes deposita variables cantidades de dinero; además, se requiere saber cuánto lleva ahorrado cada mes.
                                                          --- '''

x = 1
suma = 0

#Ingresar lo que se ahorra mes a mes, hace la suma mes a mes y al terminar automáticamente.
while x <= 12 :
    print("Ingrese lo que va a ahorrar este mes: ")
    ahorro = int(input())
    suma = ahorro + suma
    print("El ahorro acumulado hasta el mes N°", x, "es de:", suma,"pesos")
    print(' ')
    x = x + 1

#Ahorro total que logro en el año.
print("El ahorro total de este año fue de:", suma,"pesos")
          
          


