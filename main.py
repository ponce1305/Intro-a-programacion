#ejercicio1

#print ("hola mundo")

#ejercicio2
#mensaje= "hola mundo"
#print (mensaje)

#ejercicio3
#nombre = "¿cual es tu nombre? "
#mensaje = "hola " + input (nombre)
#print (mensaje)

#ejercicio4
#print (((3+2)/(2*5))**2)

#ejercicio5
#tiempo = float (input("escribir el numero de horas diarias "))
#costo = float ( input("escribir cuanto te pagan por hora "))
#pago = tiempo*costo
#print ("tu pago es: " + input(pago))

#ejercicio6
#N = int (input("introduce un numero positivo "))
#print (N*(N+1)/2)

#ejercicio7
#W = float (input("escribir el peso en Kg: "))
#H = float (input("escribir la altura en M: "))
#imc = round(float(W)/ float(H)**2,2)
#print ("tú indice de masa corporal es: ", imc)

#ejercicio8
#N = int(input("introduce un numero positivo: "))
#M = int(input("introduce un numero distinto a cero: "))
#print ( N%M, N//M)

#ejercicio9
#C = float (input("cantidad a invertir: "))
#I = float (input("cual es el interes: " ))
#A = float (input("cuantos años: "))
#R = round (float (C) * ((float (I) / 100 +1)** float(A)), 2)
#print ("tu capital es: ", R)

#ejercicio10
#P = int(input("cantidad de payasos: "))
#M = int(input("cantidad de muñecas: "))
#R = round ((int(P) * 112) + (int(M) * 75))
#print ("la cantidad total es: ", R)

#ejercicio1
#N = int(input("introducir un entero positivo: "))
#suma = int(int(N) * (int(N) + 1) / 2)
#print(suma)
#if suma>20:
#print("es un gran número!")

#ejercicio2
N = int(input("introduce un numero positivo: "))
M = int(input("introduce un numero distinto a cero: "))
C = int( N//M )
R = int( N & M )
print ( N%M, N//M)
if C < 1:
    print("El divisor es mayor al dividendo")
elif C > 1:
    print("El divisor es menor al dividendo")
elif C == 1:
    print("El divisor y el dividendo son iguales")
