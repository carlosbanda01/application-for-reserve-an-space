import data
import datetime as dt
bd = data.data

def search(dni):
    for dato in bd:
        if dato['DNI'] == dni:
            print ("Encontrado")
            return True
        else:
            return False

def val_dnitype(dni):
    if len(str(dni)) == 8:
        search(dni)
    else:
        print("DNI invalido")
        return False
    
def reserved_gate(dni):
    for dato in bd:
        if dato['DNI'] == dni:
            print("Encontrado")
            gate = dato['gate']
    return gate

def have_permission(dni):
    for dato in bd:
        if dato['DNI'] == dni:
            print("Encontrado")
            access = dato['reserva']
    return access

def day_():
    x = dt.date.today()
    x_str = f'{x.day}/{x.month}/{x.year}'
    return x_str

def available_gate():
    _day = day_()
    _time = time_()
    return val_gate(_day,_time)


def dni_read(dni):
    val_acces = val_dnitype(dni)
    if val_acces == True:
        gate = reserved_gate(dni)
        access = have_permission(dni)
        return[access,gate]
    else:
        print("Usted no tiene acceso")
        return [0,0]

def reservation_now():
    ava_g = available_gate()
    if ava_g == 0:
        print("No hya puertas disponibles")
        return [0,0]
    else:
        return [ava_g,1]
