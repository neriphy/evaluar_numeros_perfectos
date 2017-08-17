#Calculador de numeros perfectos
#Creado por @neriphy

import time


numero = int(input("¿Que numero desea evaluar? "))
start = time.time()


intentos = numero

suma = 0

intentos = numero - 1

while intentos>0:
	if numero%intentos == 0:
		suma = intentos + suma
		print("intentos",intentos,"y suma=",suma)
	"""elif numero&intentos != 0:
		intentos = intentos - 1"""

	intentos = intentos - 1



if suma == numero:
	print(numero , "es un numero perfecto")

else:
	print(numero, "no es un numero perfecto")

print(suma)

if suma == 1:
	print(numero,"es numero primo")
if suma != 1:
	print(numero,"no es numero primo")

end = time.time()

time_elapsed = end - start
time_in_miliseconds = time_elapsed * 1000

print("\nTiempo:",time_in_miliseconds)

