import reads
num_gate = 2
in_gate = 0 #puerta cerrada inicialmente
def access():
    dni = input('Ingrese su DNI: ')
    reserve = reads.dni_read(dni)
    if reserve == [0,0] & reads.search(dni) == False:
        print("El DNI no está en la base de datos")
        print("Ingrese un DNI que si esté en la base de datos")
        access()
    elif reserve == [0,0] & reads.search(dni) == True:
        _action = input("Ingresa s o n para definir si quieres reservar ahora")
        if _action == 's': 
            reads.reservation_now()
        else:
            access()
    else:
        access_val = reserve[0]
        gate = reserve[1]
    return [access_val,gate]

def save():
    return save