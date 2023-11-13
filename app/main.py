import assets
#El numero de grupo y demas especificaciones requeridas estan en readme.dm
def main():
    print("Iniciando Programa....")
    results=assets.access()# funcion que inicia el sistema
    assets.save()#funcion que guarda los datos
    #send_to_arduino(results[1])#enviamos a arduino el valor de la puerta

if __name__ == '__main__':
    main()
