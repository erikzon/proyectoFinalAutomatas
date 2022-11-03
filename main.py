# TODO
########NIVEL NORMAL:
# validar que los estados no se llamen igual
# validar que los estados solo sean signos y letras mayusculas
# validar que solo se ingrese un estado inicial y que este pertenezca a los estados declarados
# validar que los estados finales pertenezcan a los estados declarados
# validar que el alfabeto no tenga simbolos repetidos

########NIVEL DIFICIL:
# hacer que despues de validar una cadena vuelva a preguntar por otra cadena o que reciba varias y valide todas una por una

########NIVEL DIOS:
# tratar de que el alfabeto reciba mas de 1 caracter por simbolo
# tratar de dibujar el diagrama del automata

def proyectoFinal():
    estados = input("Ingrese los estados separados por comas:\n")
    estadosArray = estados.split(",")

    # recibir estado inicial
    estadoInicial = input("Ingrese el estado inicial:\n")

    # recibir el estadofinal
    estadoFinal = input("Ingrese el o los estados finales separados por coma:\n")
    estadosFinalesArray = estadoFinal.split(",")

    # recibir el alfabeto
    alfabeto = input("Ingrese el alfabeto separados por coma:\n")
    alfabetoArray = alfabeto.split(",")

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
                estadoActual = destino[estadoActual].split(',')[simbolo[estadoActual].split(',').index(caracter)]
            else:
                estadoActual = destino[estadoActual]
        else:
            # no existe simbolo para ese estado asi que la cadena es invalida
            cadenaValida = False

    # se pone else despues de un for para que ejecute esta linea al terminar el bucle
    if estadoActual in estadoFinal:
        cadenaValida = True
    else:
        cadenaValida = False
    print("la cadena " + cadena + " es valida") if cadenaValida else print("la cadena " + cadena + " es invalida.")


if __name__ == '__main__':
    proyectoFinal()
