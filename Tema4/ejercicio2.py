#EN EL SIGUIENTE EJERCICIO SE NOS PIDE CREAR TRES ARBOLES, UNO CON LOS NOMBRE, NUMERO Y DEBILIDAD

#Cogemos el csv y lo dividimos en una lista de listas
import csv
import numpy as np
with open('/Users/hectorbernaltrujillo/Documents/informática/Programación python/ff/evaluacion_tema4/Tema4/pokemon.csv', 'r') as f:
    reader = csv.reader(f)
    lista = list(reader)

#Creamos una lista con los nombres de los pokemons
nombres = []
for i in range(1, len(lista)):
    nombres.append(lista[i][1]) #Cogemos la columna 1 que es la de los nombres

#Creamos una lista con los numeros de los pokemons
numeros = []
for i in range(1, len(lista)):
    numeros.append(lista[i][0]) #Cogemos la columna 0 que es la de los numeros

#Creamos una lista con las debilidades de los pokemons
debilidades = []
for i in range(1, len(lista)):
    debilidades.append(lista[i][2]) #Cogemos la columna 2 que es la de las debilidades


#Creamos tres arboles donde sus indices son el nombre, el numero y la debilidad

class nodoArbol(object):

    def __init__(self, info):
        self.info = info
        self.izq = None
        self.der = None

def insertar_nodo(raiz, dato):
    if raiz == None:
        raiz = nodoArbol(dato)
    elif dato < raiz.info:
        raiz.izq = insertar_nodo(raiz.izq, dato)
    else:
        raiz.der = insertar_nodo(raiz.der, dato)
    return raiz

def buscar(raiz,clave):
    pos= None 
    if raiz != None:
        if clave == raiz.info:
            pos = raiz
        elif clave < raiz.info:
            pos = buscar(raiz.izq,clave)
        else:
            pos = buscar(raiz.der,clave)
    return pos


def inorden(raiz): #Recorrido inorden: esta funcion nos debuelve una lista con los datos del arbol en orden de menor a mayor
    if raiz != None:
        inorden(raiz.izq)
        print(raiz.info)
        inorden(raiz.der)

def por_nivel(raiz):
    '''Funcion que nos imprime los datos del arbol por niveles'''
    cola = []
    cola.append(raiz)
    while len(cola) > 0:
        nodo = cola.pop(0)
        print(nodo.info)
        if nodo.izq != None:
            cola.append(nodo.izq)
        if nodo.der != None:
            cola.append(nodo.der)

def mostrar_tipo(dato):
    '''Funcion que muestra todos los tipos de pokemons y cantidad de cada uno'''
    tipos = []
    for i in range(1, len(lista)):
        tipos.append(lista[i][3])
    tipos = np.array(tipos)
    tipos = np.unique(tipos)
    for i in range(len(tipos)):
        print(tipos[i], ':', list(tipos).count(tipos[i]))
    

#Creamos el arbol de nombres

raiz = None
for i in range(len(nombres)):
    raiz = insertar_nodo(raiz, nombres[i])

#Creamos el arbol de numeros

raiz2 = None
for i in range(len(numeros)):
    raiz2 = insertar_nodo(raiz2, numeros[i])

#Creamos el arbol de debilidades

raiz3 = None
for i in range(len(debilidades)):
    raiz3 = insertar_nodo(raiz3, debilidades[i])

#Mostramos los arboles

print('Arbol de nombres')
por_nivel(raiz)
print('Arbol de numeros')
por_nivel(raiz2)
print('Arbol de debilidades')
por_nivel(raiz3)

#Mostramos los tipos de pokemon y su cantidad

mostrar_tipo(lista)

#Mostramos los pokemons que son de tipo agua

print('Pokemons de tipo agua')
for i in range(1, len(lista)):
    if lista[i][3] == 'Water':
        print(lista[i][1])

#Mostramos los pokemons que son de tipo fuego

print('Pokemons de tipo fuego')
for i in range(1, len(lista)):
    if lista[i][3] == 'Fire':
        print(lista[i][1])

#Mostramos los pokemons que son de tipo planta

print('Pokemons de tipo planta')
for i in range(1, len(lista)):
    if lista[i][3] == 'Grass':
        print(lista[i][1])

#Mostramos los pokemons que son de tipo electrico

print('Pokemons de tipo electrico')
for i in range(1, len(lista)):
    if lista[i][3] == 'Electric':
        print(lista[i][1])

#realizamos una busqueda en el arbol de nombres por proximidad

print('Busqueda por proximidad')
print('Introduce el nombre del pokemon')
nombre = input()
for i in range(len(nombres)):
    if nombre in nombres[i]:
        print(nombres[i])

#realizamos un listado en orden ascedente por numero de pokemon

print('Listado de pokemons por numero')
inorden(raiz2)

#realizamos un listado en orden ascedente por nombre de pokemon

print('Listado de pokemons por nombre')
inorden(raiz)

#realizamos un listado por nivel por nombre de pokemon

print('Listado de pokemons por nivel')
por_nivel(raiz)

#