from lecturainput import lectura_input
from gram1 import hash1, parsing_table1
from gram2 import hash2, parsing_table2
from gram3 import hash3, parsing_table3

def Procesamiento(lista_de_listas):
    for sublista in lista_de_listas:
        if sublista:
            primer_caracter = sublista[0][0]
            sublista_aux = sublista[1:]
            if primer_caracter == '#':
                resultado_hash1 = hash1(sublista_aux)
                table1 = parsing_table1(resultado_hash1)
                print(table1)
            elif primer_caracter == '%':
                resultado_hash2 = hash2(sublista_aux)
                table2 = parsing_table2(resultado_hash2)
                print(table2)
            elif primer_caracter == '&':
                resultado_hash3 = hash3(sublista_aux)
                table3 = parsing_table3(resultado_hash3)
                print(table3)
            else:
                print("Operación no reconocida")

arreglo_bidimensional = lectura_input('Input.txt')
Procesamiento(arreglo_bidimensional)