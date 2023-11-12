import reads
#num_gate = 2
#in_gate = 0 #puerta cerrada inicialmente
def access():
    dni = input('Ingrese su DNI: ')
    reserve = reads.dni_read(dni)#ahora hay 3 columnas de reserve [0,0,0], [0,0,1] u otro
    #Cuando no tiene reservas y el DNI no esta en la base de datos (caso yo)
    if reserve[0] == False and reserve[1]==False:
        print("El DNI no se encontro en la base de datos")
        print("Ingrese un DNI que si esté en la base de datos")
        access()
    #Caundo no tiene reservas y el DNI si esta en la base de datos (caso piedra)
    elif reserve[0] == True and reserve[1] ==False:
        _action = input("Ingresa si o no para definir si quieres reservar ahora (debe escribir: <<si>>, no sí)")
        if _action == 'si': 
            access_val=reads.reservation_now()[1]#si se logra la reserva, esto sera 1, sino 0
            gate_val=reads.reservation_now()[0]#si se logra la reserva, esto sera 1 o 2, sino 0
            if gate_val==0:
                print("No hay campo deportivo disponible")
        else:
            print("Ha decidido que no va a reservas")
            print("Iniciando el programa...")
            access()
    #Cuando si tiene reserva (caso sofia o klever)
    else:
        access_val = reserve[0]
        gate_val = reserve[1]
        if gate_val==1:
            fecha="11/11/23"
        else:
            fecha="10/11/23"
        if gate_val !=0:
            print(f"Usted tiene reservado el campo {gate_val} para {fecha} ")
        return [access_val,gate_val]#puerta abrir o puerta cerrar

def save():

    print("Cerrando el programa")