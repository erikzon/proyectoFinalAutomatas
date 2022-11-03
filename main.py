def proyectoFinal(name):
    # Use a breakpoint in the code line below to debug your script.
    estados = input("Ingrese los estados separados por comas:\n")
    estadosArray = estados.split(",")
    estadoInicial = input("Ingrese el estado inicial:\n")
    estadoFinal = input("Ingrese el o los estados finales separados por coma:\n")
    estadosFinalesArray = estadoFinal.split(",")
    alfabeto = input("Ingrese el alfabeto separados por coma:\n")
    alfabetoArray = alfabeto.split(",")
    print(f'Los estados son los siguientes: {estadosArray}')
    print(f'El estado inicial es: {estadoInicial}')
    print(f'Los estados finales son: {estadosFinalesArray}')
    print(f'El alfabeto es: {alfabetoArray}')
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    proyectoFinal('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
