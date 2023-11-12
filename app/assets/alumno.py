#alumno.py
#---------
#this script will asks for multiple data and with that will calculate the year of graduation of the student

import re
# Solicitar datos al usuario
nombre_alumno= input("Ingrese el nombre del alumno: ")
año_ingreso = int(input("Ingrese el año de ingreso: "))
semestre = int(input("Ingrese el semestre actual: "))

#Creo mis funciones de validacion
patron_fecha = r"\d{2}/\d{2}/\d{4}"

while True:
    fecha_nacimiento=input("Ingrese la fecha de su nacimiento en formato (DD/MM/AAAA): ")

    if re.match(patron_fecha, fecha_nacimiento):
        break
    else:
        print("La fecha no esta en el formato correcto (DD/MM/YYYY). Por favor, inténtalo de nuevo.")

def val_year(data):
	try:
		if len(data) == 4:
			data_int = int(data)
			print("Se guardo el dato")
			print(data_int)
		else:
			print("El valor no esta en el rango adecuado")
	except:
		print("El valor ingresado no es un numero")
		
val_year(año_ingreso)

def val_semester(dato):
	try:
		dato_int = int(dato)
		if dato_int in range(0,11):
			print("Validacion de semestrecorrecta")
			print(dato_int)
		else:
			raise Exception("El valor no esta en el rango correcto")
	except:
		 raise TypeError("El valor no es un número")

val_semester(semestre)

# Calcular posible año de egreso (4 años desde el año de ingreso)
tiempo_faltante=(10-semestre)/2
año_actual=año_ingreso+(semestre/2)
año_egreso = (año_actual) + tiempo_faltante-1

# Calcular edad de egreso (restando el año de nacimiento del año de egreso)
fecha_lista = fecha_nacimiento.split("/")
año_nacimiento = int(fecha_lista[2])
edad_egreso = año_egreso - año_nacimiento

# Guardar los datos en una lista
lista = [nombre_alumno, fecha_nacimiento, año_ingreso, semestre, año_egreso, edad_egreso]

# Imprimir la lista con los datos
print("Lista de datos del alumno:")
print("Nombre del alumno:", lista[0])
print("Fecha de nacimiento:", lista[1])
print("Año de ingreso:", lista[2])
print("Semestre actual:", lista[3])
print("Posible año de egreso:", lista[4])
print("Edad de egreso:", lista[5])