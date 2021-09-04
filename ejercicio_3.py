''' Ejercicio 3:
      Una multitienda tiene una promoción: a todos los trajes que tienen un precio superior a $10000 se les
      aplicará un descuento de 15 %, a todos los demás se les aplicará sólo 8 %. Realice un programa para
      determinar el precio final que debe pagar una persona por comprar un traje y de cuánto es el descuento
      que obtendrá. Pida por lo menos ingresar 3 elementos.
                                                              --- '''

trajes = 0

# Número de trajes que el cliente comprará
print(" Ingrese la cantidad de trajes que va a cancelar, se recomiendo ingresar a los menos 3 elementos: ")
n = int(input())

print(' ')

# Cálculos para saber cuanto se tiene que pagar por cada traje y su descuento respectivo.
while trajes < n :
    print(" Ingrese el precio del traje a comprar: ")
    precio = int(input())
    if precio > 10000 :
        descuento = precio * 0.15
    else:
        descuento = precio * 0.8
    print(' ')
    precio_final = precio - descuento
    print(" El descuento que ha sido aplicado es de: ", descuento, " pesos ")
    print(" El precio final por el traje seria de: ", precio_final, " pesos ")
    print(' ')
    trajes = trajes + 1

 

