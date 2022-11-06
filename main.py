# TODO
# NIVEL NORMAL:
# validar que los estados no se llamen igual
# validar que los estados solo sean signos y letras mayusculas
# validar que solo se ingrese un estado inicial y que este pertenezca a los estados declarados
# validar que los estados finales pertenezcan a los estados declarados
# validar que el alfabeto no tenga simbolos repetidos
# validar que las entradas que recibe en la linea 36 y 38 correspondan con las sugerencias (que no ingrese estado en
# los simbolos)

# NIVEL DIFICIL:
# hacer que despues de validar una cadena vuelva a preguntar por otra cadena o que reciba varias y valide todas una por una
def proyectoFinal():
    #recibir estados:
    global flag
    flag = False
    global estado
    estado = ""
    while flag == False:
        protoestados = input("Ingrese los estados separados por comas:\n")
        if protoestados.upper() in estado.upper():
            print("#Ya existe este estado")
        else:
            print("Estado agregado")
            estado = estado + protoestados
            estadosArray = estado.upper().split(",")

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
    global estadoInicial
    estadoInicial=""
    while flagI == False:
        protoestadoInicial = input("Ingrese el estado inicial:\n")
        if protoestadoInicial.upper() in estadosArray:
            print("Si esta dentro de los estados")
            estadoInicial = protoestadoInicial.upper()
            flagI = True
        else:
            print("#No esta dentro de los estados")
            flagI = False
    print("--Sus estados Iniciales son: ", estadoInicial)



    # recibir el estados finales
    global flagE
    flagE = False
    global estadoFinal
    estadoFinal = ""
    while flagE == False:
        protoestadoFinal = input("Ingrese el o los estados finales separados por coma:\n")
        if estadosArray in protoestadoFinal.upper().split(","):
            estadoFinal = protoestadoFinal.upper().split(",")
            estadosFinalesArray = estadoFinal
            flagE = True
        else:
            print("#No esta dentro de los estados")
            flagE = False
    print("--Sus estados Finales son: ", estadoFinal)


    # recibir el alfabeto
    global flagAl
    flagAl = False
    global alfabeto
    alfabeto = ""
    while flagAl == False:
        protoalfabeto = input("Ingrese el alfabeto aceptado separados por comas:\n")
        if protoalfabeto.lower() in alfabeto.lower():
            print("#Ya existe este estado")
        else:
            print("Estado agregado")
            alfabeto = alfabeto + protoalfabeto
            alfabeto = alfabeto.lower().split(",")
            alfabetoArray = alfabeto

        seguir = input("////Desea ingresar mas estados? \n 1. Si \n 0. No ")
        if seguir == "1":
            flagAl = False
        else:
            if seguir == "0":
                print("--Sus estados definidos son: ", estadosArray)
                flagAl = True
            else:
                print("##Error, por favor escriba con número \n //// 1 = Si \n //// 0 = No")



    # recibir las transiciones, se almacenaran en diccionarios
    destino = {}
    simbolo = {}
    for estado in estadosArray:
        destino[estado] = input(
            f"ingrese los destinos para el estado: {estado} separados por coma, pueden ser: {estadosArray}")
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
            else:
                print("##Error, por favor escriba con número \n 1 = Si \n 0 = No")


if __name__ == '__main__':
    proyectoFinal()
