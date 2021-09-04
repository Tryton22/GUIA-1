''' Ejercicio 1:

      Realice un programa en Phyton para determinar cuánto se debe pagar por equis
      cantidad de lápices considerando que si son más de 1000 el costo es de 85 pesos;
      de lo contrario el precio es de 95 pesos
      
                              ----- '''

# Ingresar la cantidad de lápices que quiere el cliente.
print("Ingrese la cantidad de lápices que va a comprar el usuario")

lapices = int(input())

# Calcular el valor de cada lápiz según la cantidad que quiere el cliente.
if lapices >= 1000 :
    lapicesA = lapices * 85
else:
    lapicesA = lapices * 90

# La cantidad de lápices del cliente y lo que tiene que pagar en total.  
print ("El total de lapices que se va a comprar es de", lapices, "unidades")
print("Y el total a pagar por el usuario es de:", lapicesA, "pesos chilenos")
