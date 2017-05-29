suma = 0 
bandera = True 
while bandera :
	numero = int (input("Ingrese el valor a sumar : "))
	suma = suma + numero 
	salir = int (input("Presione -1 si desea salir : "))
	if salir == -1 :
		bandera = False 

print ("Los valores sumados son igual a ", suma )



