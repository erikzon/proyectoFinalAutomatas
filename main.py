def proyectoFinal():
    #recibir estados:
    global flag
    flag = False
    global estado
    estado = ""
    estadosArray=[]
    while flag == False:
        protoestados = input("Ingrese los estados de uno en uno:\n").upper()
        if protoestados.upper() in estado.upper():
            print("#Ya existe este estado")
        else:
            print("Estado agregado")
            estadosArray.append(protoestados.upper())
        seguir = input("////Desea ingresar mas estados? \n//// 1. Si \n ////0. No ")
        if seguir == "1":
            flag = False
        else:
            if seguir == "0":
                print("--Sus estados definidos son: ", estadosArray)
                flag = True
            else:
                print("##Error, por favor escriba con número \n//// 1 = Si \n //// 0 = No")



    # recibir estado inicial
    global flagI
    flagI = False
    while flagI == False:
        estadoInicial = input("Ingrese el estado inicial:\n").upper()

        if estadoInicial.upper() in estadosArray:
            print("Si esta dentro de los estados")
            estadoInicial = estadoInicial.upper()
            flagI = True
        else:
            print("#No esta dentro de los estados")
            flagI = False
    print("--Su estado Inicial definido es: ", estadoInicial)



    # recibir el estados finales
    global flagE
    flagE = False
    estadosFinalesArray = []
    while flagE == False:
        estadoFinal = input("Ingrese el o los estados finales de uno en uno:\n").upper()
        if estadoFinal.upper() in estadosArray:
            estadosFinalesArray.append(estadoFinal.upper())
            flagE = True
        else:
            print("#No esta dentro de los estados")
            flagE = False

        seguirE = input("Desea seguir? \n//// 1 = Si \n //// 0 = No")
        if seguir == "1":
            flag = False
        else:
            if seguir == "0":
                print("--Sus estados Finales definidos son: ", estadosFinalesArray)
                flag = True
            else:
                print("##Error, por favor escriba con número \n//// 1 = Si \n //// 0 = No")


    # recibir el alfabeto
    global flagAl
    flagAl = False
    global alfabeto
    alfabeto = ""
    alfabetoArray=[]
    while flagAl == False:
        alfabeto = input("Ingrese el alfabeto aceptado de uno en uno:\n").upper()
        if alfabeto.lower() in alfabetoArray:
            print("#Ya existe este estado")
        else:
            print("Caracter de alfabeto agregado")
            alfabetoArray.append(alfabeto.lower())

        seguir = input("////Desea ingresar mas alfabeto? \n 1. Si \n 0. No ")
        if seguir == "1":
            flagAl = False
        else:
            if seguir == "0":
                print("--Su alfabeto definido es: ", alfabetoArray)
                flagAl = True
            else:
                print("##Error, por favor escriba con número \n //// 1 = Si \n //// 0 = No")



    # recibir las transiciones, se almacenaran en diccionarios
    destino = {}
    simbolo = {}
    for estado in estadosArray:
        destino[estado] = input(
            f"ingrese los destinos para el estado: {estado} separados por coma, pueden ser: {estadosArray}").upper()
        simbolo[estado] = input(
            f"ingrese los simbolos para el estado: {estado} separados por coma, puede ser: {alfabetoArray}")



    # dar un resumen de la informacion recibida:
    print('#############RESUMEN#############')
    print(f'Los estados son los siguientes: {estadosArray}')
    print(f'El estado inicial es: {estadoInicial}')
    print(f'Los estados finales son: {estadosFinalesArray}')
    print(f'El alfabeto es: {alfabetoArray}')
    print(f'Los destinos de los estados son: {destino}')
    print(f'Los simbolos para los estados son: {simbolo}')
    print('#########FIN DEL RESUMEN##########')



    global flagCad
    flagCad = False
    while flagCad==False:
        # pedimos la cadena para validarla
        cadena = input("Ingrese la cadena por validar:\n")
        cadenaValida = True


        # validamos caracter por caracter para ver si la cadena es valida
        estadoActual = estadoInicial
        for position, caracter in enumerate(cadena):

            if position == 0:
                print('inicio')

            elif position == len(cadena) - 1:
                print('final')

            if caracter in simbolo[estadoActual]:
                # si es valido entonces seteamos el destino
                # si existe mas de un destino obtenemos el destino correspondiente a la posicion a la que se declaro
                if len(destino[estadoActual]) > 1:
                    estadoActual = destino[estadoActual].split(
                        ',')[simbolo[estadoActual].split(',').index(caracter)]
                else:
                    estadoActual = destino[estadoActual]
            else:
                # no existe simbolo para ese estado asi que la cadena es invalida
                cadenaValida = False

        # al finalizar el for se valida que el estado actual sea el estado final
        if estadoActual in estadoFinal and cadenaValida == True:
            cadenaValida = True
        else:
            cadenaValida = False
        print("la cadena " + cadena +
              " es valida") if cadenaValida else print("la cadena " + cadena + " es invalida.")


        newstring = input("////Desea ingresar una nueva cadena: \n ////1. Si \n ////0. No")
        if newstring == "1":
            flagCad=False
        else:
            if newstring == "0":
                print("Fue un gusto, adios")
                flagCad = True
            else:
                print("##Error, por favor escriba con número \n 1 = Si \n 0 = No")


if __name__ == '__main__':
    proyectoFinal()
