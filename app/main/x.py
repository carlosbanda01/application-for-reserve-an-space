import data
bd=data.data
a = '70398195'
def search(dni):
    for dato in bd:
        if dato['DNI'] == dni:
            print ("Encontrado")
            i = bd[i]
            return bd[i]
        else:
            return False
    if bd[i]['Reserva'] == 0:
        print("no tiene reserva")
    else:
        print("si tiene reserva")
search(a)

