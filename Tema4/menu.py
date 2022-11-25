from ejercicio1 import *
from ejercicio2 import *
import time

import csv 
import numpy as np
with open('/Users/hectorbernaltrujillo/Documents/informática/Programación python/ff/evaluacion_tema4/pokemon.csv', 'r') as f:
    reader = csv.reader(f)
    lista = list(reader)

#CREAMOS UNA LISTA CON LOS NOMBRES:
nombres= []
for i in range(1, len(lista)):  
    nombres.append(lista[i][1]) #Cogemos la columna 1 que es la de los nombres

#CREAMOS UNA LISTA CON LOS NUMEROS:
numeros= []
for i in range(1, len(lista)): 
    numeros.append(lista[i][0]) #Cogemos la columna 0 que es la de los numeros

#CREAMOS UNA LISTA CON LAS DEBILIDADES:
tipos= []
for i in range(1, len(lista)): 
    tipos.append(lista[i][2]) #Cogemos la columna 2 que es los tipos

raiz = None
for i in range(len(nombres)):
    raiz = insertar_nodo(raiz, nombres[i])

#NUMEROS:
raiz2 = None
for i in range(len(numeros)):
    raiz2 = insertar_nodo(raiz2, numeros[i])

#TIPOS:
raiz3 = None
for i in range(len(tipos)):
    raiz3 = insertar_nodo(raiz3, tipos[i])


def iniciar():

    while True:

        print('----------------------------------------')
        print('-----------------MENU-------------------')
        print('----------------------------------------')
        print('[1] Ejercicio 1: Codificar y decodificar')
        print('[2] Ejercicio 2: Pokemons')
        print('[3] Ejercicio 3: Las 7 Maravillas')
        print('[4] Ejercicio 4: salir del programa')
        print('----------------------------------------')

        opcion = input('Introduce una opcion: ')

        if opcion == '1':
            print('.....Cargando.....')
            time.sleep(2)
            simbolos= ['A', 'F', '1', '3', 'O', 'M', 'T']
            frecuencias= [0.2, 0.17, 0.13, 0.21, 0.05, 0.09, 0.15]
            raiz= arbol_huffman(simbolos, frecuencias)
            print('\nObtenemos los siguientes códigos por cada símbolo:')
            print('A: ', codificar('A', raiz))
            print('F: ', codificar('F', raiz))
            print('1: ', codificar('1', raiz))
            print('3: ', codificar('3', raiz))
            print('0: ', codificar('0', raiz)) #TODO: Falla al codificar el 0 
            print('M: ', codificar('M', raiz))
            print('T: ', codificar('T', raiz))

            while True:
                print('¿Quieres codificar algun mensaje? (SI/NO)')
                respuesta= input()
                if respuesta.upper()== 'SI':
                    print('tabla de simbolos: ', simbolos)
                    print('Introduce el mensaje a codificar: ')
                    mensaje= input()
                    print('Mensaje codificado: ', codificar(mensaje, raiz))
                    print('Mensaje decodificado: ', decodificar(codificar(mensaje, raiz), raiz))
                elif respuesta.upper()== 'NO':
                    print('....Volviendo al menu....')
                    break
                else:
                    print('Introduce SI o NO')


            
        elif opcion == '2':
            
            print('.....Cargando.....')
            time.sleep(2)
            while  True:
                print('[1] Buscar pokemos por nombre o por proximidad')
                print('[2] Buscar pokemons por tipo (Fuego, Agua, Planta y Eléctrico)')
                print('[3] Mostrar listado por nombre en forma ascendente') 
                print('[4] Mostrar listado por número en forma ascendente')
                print('[5] Mostrar los Pokemos que son debiles a (Jolteon, Lycanroc y Tyrantrum)')
                print('[6] Mostrar todos los tipos de pokemos y la cantidad de pokemos que hay de cada tipo')
                print('[7] Listado de nombres por nivel')
                print('[8] Nada')

                opcion = input('Introduce una opcion: ')

                if opcion == '1':
                    for i in [3,2,1]:
                        time.sleep(i)
                        print(f'.....Cargando en {i}.....')
                    print('Introduce el nombre del pokemon que quieres buscar: ')
                    nombre = input()
                    proximidad_nombres(nombre, nombres)

                elif opcion == '2':
                    for i in [3,2,1]:
                        time.sleep(i)
                        print(f'.....Cargando en {i}.....')
                    print('Introduce el tipo de pokemon que quieres buscar: ')
                    tipo = input()
                    tipo_pokemon(tipo, tipos)

                elif opcion == '3':
                    for i in [3,2,1]:
                        time.sleep(i)
                        print(f'.....Cargando en {i}.....')
                    print('Listado de pokemos por nombre: ')
                    inorden(raiz)
                
                elif opcion == '4':
                    for i in [3,2,1]:
                        time.sleep(i)
                        print(f'.....Cargando en {i}.....')
                    print('Listado de pokemos por numero: ')
                    inorden(numeros)

                elif opcion == '5':
                    for i in [3,2,1]:
                        time.sleep(i)
                        print(f'.....Cargando en {i}.....')
                    print('Los pokemos que son debiles a Jolteon, Lycanroc y Tyrantrum son: ')
                    debil('Jolteon', 'Lycanroc', 'Tyrantrum')

                elif opcion == '6':
                    for i in [3,2,1]:
                        time.sleep(i)
                        print(f'.....Cargando en {i}.....')
                    unicos = {}
                    unicos = valores_unicos(raiz3, unicos)
                    print('Hay', len(unicos), 'pokemons diferentes')

                elif opcion == '7':
                    for i in [3,2,1]:
                        time.sleep(i)
                        print(f'.....Cargando en {i}.....')
                        por_nivel(raiz)

                elif opcion == '8':
                    break

                else:
                    print('Opcion no valida')

        elif opcion == '3':
            


iniciar()


                    








