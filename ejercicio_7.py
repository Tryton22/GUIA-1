''' Ejercicio 7:
    El buen gordito” ofrece hamburguesas sencillas, dobles y triples, las cuales tienen un costo de $2000,
    $2500 y $3000 respectivamente. La empresa acepta tarjetas de crédito con un cargo de 5 % sobre la
    compra. Suponiendo que los clientes adquieren solo un tipo de hamburguesa, realice un algoritmo para
    determinar cuánto debe pagar una persona por N hamburguesas.
                                                               --- '''

error = 0

# El número de hamburguesas que va a pedir el cliente.
print(" Ingrese el número de hamburguesas que el cliente va a pedir: ")
numero = int(input())

print(' ')

# Ingresar el tipo de hamburguesa que quiere el cliente.
print(" Ingresa un tipo de hamburguesa para pedir: ")
print(" Número 1: Hamburguesa Sencilla  $2000. ")
print(" Número 2: Hamburguesa Doble  $2500. ")
print(" Número 3: Hamburguesa Triple  $3000. ")

tipo = int(input())

print(' ')

# El cliente quiere hamburguesa sencilla.
if tipo == 1 :
    total = numero * 2000
 
# El cliente quiere hamburguesa doble.
elif tipo == 2 :
    total = numero * 2500

# El cliente quiere hamburguesa triple.
elif tipo == 3 :
    total = numero * 3000

# El cajero tuvo un error de tipeo. 
else:
    print(" Ingrese un tipo de hamburguesa disponible en el local ")
    error = 1
    
print(' ')

# Ingresar el método con que pagará el cliente
if error == 0 :
    print(" Ingrese el método de pago del cliente: ")
    print(" Efectivo = 1 ")
    print(" Débito = 2 ")
    print(" Crédito = 3 ")
    
tipo = int(input())

print(' ')

# El cliente eligió pagar con efectivo.
if tipo == 1 :
    print(" El total a pagar por las ", numero," hamburguesas es de: ", total," pesos ")

# El cliente eligió pagar con tarjeta de débito.
elif tipo == 2 :
    print(" El total a pagar por las ", numero," hamburguesas es de: ", total," pesos ")

# El cliente eligió pagar con tarjeta de crédito.
elif tipo == 3 :
    cargo = total * 0.5
    print(" El total a pagar por las ", numero," hamburguesas es de: ", total + cargo," pesos ")
    print(" El cargo de la tarjeta fue de: ", cargo," pesos ")

# El cajero tuvo un error de tipeo.
else:
    print(" Ingrese un método de pago disponible ")
    
    
    


