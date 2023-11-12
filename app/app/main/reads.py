import data
import datetime as dt
bd = data.data
tm=data.times

#funcion que busca el DNI en la base de datos
def search(dni):
    for dato in bd:
        if dato['DNI'] == dni:
            print("DNI Encontrado en la base de datos")
            return True
    print("DNI no encontrado en la base de datos")
    return False

#valida si el DNI tiene 8 digitos y si si lo tiene, va a la funcion search
def val_dnitype(dni):
    if len(str(dni)) == 8:
        print("DNI valido: 8 digitos")
        return search(dni)
    else:
        print("DNI invalido")
        return False

#Funcion que asigna el valor a gate correspondiente dependiendo del DNI ingresado, que debe tener reserva    
def reserved_gate(dni):
    for dato in bd:
        if dato['DNI'] == dni:
            print("DNI Encontrado en la base de datos de reserva")
            num_gate = dato['Gate']
    return num_gate

def have_permission(dni):
    for dato in bd:
        if dato['DNI'] == dni:
            print("su DNI tiene permiso de acceso")
            num_access = dato['Reserva']
    return num_access

def day_():
    x = dt.date.today()
    x_str = f'{x.day}/{x.month}/{x.year}'
    return x_str

def time():
    hour_ = dt.datetime.now()
    if int(hour_.hour)>12:
        str_hour = f'{hour_.hour-12}:00pm'
    elif int(hour_.hour)<12:
        str_hour = f'{hour_.hour}:00am'
    else:
        str_hour = f'{hour_.hour}:00m'
    return str_hour

def available_gate():
    return val_gate("10/11/23","9:00pm")

def val_gate(selected_day, selected_time):
    available_gates = []  # Inicializamos una lista para almacenar los valores de gates_av1
    for day in tm:
        if day['day'] == selected_day:
            for time in day['times']:
                if time['time'] == selected_time:
                    for gate in time['gates']:
                        if gate['reserva'] == 0:
                            gates_av1 = gate['gate']
                            available_gates.append(gates_av1)  # Agregamos el valor a la lista
                            print(f"Está disponible el campo: {gates_av1}")
    return available_gates  # Devolvemos la lista de valores encontrados
   
#Lee el DNI y primero comprueba su validez para posteriormente reservar
def dni_read(dni):
    print("Leyendo DNI......")
    val_acces = val_dnitype(dni)
    if val_acces == True:
        gate = reserved_gate(dni)#devuelve la cancha
        access = have_permission(dni)#devuelve si tiene acceso
        return[access,gate]
    else:
        print("Usted no tiene acceso")
        return [0,0]

def reservation_now():
    ava_g = available_gate()
    if ava_g == 0:
        print("No hay puertas disponibles")
        return [0,0]
    else:
        print("Existen 1 o mas campos disponibles para reservar:")
        print(ava_g)
        return [1,1]
