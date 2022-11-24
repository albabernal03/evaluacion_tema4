from ejercicio1 import *
from ejercicio2 import *
import time # Importamos la libreria time para poder usar la funcion sleep 


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
            print('.....Cargando.....').sleep(2)
            mensaje= input('Introduce el mensaje a codificar: ')
            simbolos= ['A', 'F', '1', '3', 'O', 'M', 'T']
            frecuencias= [0.2, 0.17, 0.13, 0.21, 0.05, 0.09, 0.15]
            raiz= arbol_huffman(simbolos, frecuencias)
            codigo= codificar(mensaje, raiz)
            print(codigo)
            mensaje= decodificar(codigo, raiz)
            print(mensaje)

        elif opcion == '2':
            print('.....Cargando.....').sleep(2)
            while  True:
                print('[1] Buscar pokemos por nombre o por proximidad')
                print('[2] Buscar pokemons por tipo (Fuego, Agua, Planta y Eléctrico)')
                print('[3] Mostrar listado por nombre ')
                print('[4] Mostrar listado por número')
                print('[5] Mostrar los Pokemos que son debiles a (Jolteon, Lycanroc y Tyrantrum)')
                print('[6] Mostrar todos los tipos de pokemos y la cantidad de pokemos que hay de cada tipo')
                print('[7] Listado de nombres por nivel')
                print('[8] Nada')

                opcion = input('Introduce una opcion: ')

                if opcion == '1':
                    print('.....Cargando.....').sleep(2)
                    nombre = input('Introduce el nombre del pokemon: ')
                    proximidad_nombres(nombre)


iniciar()
                    








