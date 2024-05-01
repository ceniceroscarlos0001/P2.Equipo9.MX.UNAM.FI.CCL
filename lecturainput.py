def lectura_input(ruta):
    with open(ruta, 'r') as archivo:
        arreglo_bidimensional = [linea.strip().split() for linea in archivo]
    return arreglo_bidimensional
