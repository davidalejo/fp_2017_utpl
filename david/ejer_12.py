suma = 0 
bandera = True 
cadena = 0
cadena_2 = 0 
while bandera :
	numero = int (input("Ingrese el valor a sumar : "))
	suma = suma + numero 
	cadena = print ("Valor ingresado  : ", numero )
	cadena_2 = cadena_2 + numero
	salir = int (input("Presione -1 si desea salir : "))
	if salir == -1 :
		bandera = False 

print ("El resultado es : ", cadena_2)
print ("Los valores sumados son igual a ", suma )
