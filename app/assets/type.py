v_1=input("escribe una variable: ")
try:
	v_1_int=int(v_1)
	print("Es un entero")

except:
	try:
		v_1_float=float(v_1)
		print("es un float")
	except:
		print("es un string")


