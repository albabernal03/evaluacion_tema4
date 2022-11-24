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


#CREAMOS EL ARBOL:

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

    while len(cola) != 0:
        nodo = cola.pop(0)
        print(nodo.info)
        if nodo.izq != None:
            cola.append(nodo.izq)
        if nodo.der != None:
            cola.append(nodo.der)

def preorden(raiz): #Recorrido preorden: nos genera una replica del arbol
    if raiz != None:
        print(raiz.info)
        preorden(raiz.izq)
        preorden(raiz.der)


#APARATADO A:

#creamos tres arboles, uno con los nombres, otro con los numeros y otro con las debilidades

#NOMBRES:
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




#APARTADO B:

#Buscamos el pokemon que queremos por su numero y nos devuelve su nombre y su tipo:
def informacion_pokemon_numero(numero, numeros):
    if numero in numeros:
        posicion = numeros.index(numero)
        nombre = nombres[posicion]
        tipo = tipos[posicion]
        print('El pokemon numero', numero, 'se llama', nombre, 'y es de tipo', tipo)
    else:
        print('El pokemon no existe')

#Buscamos por proximidad el pokemon que queremos por su nombre, es decir si ponemos bul imprime todos con bul y nos devuelve su numero y su tipo:

def proximidad_nombres(nombre, nombres):
    for i in range(len(nombres)):
        if nombre in nombres[i]:
            posicion = nombres.index(nombres[i])
            numero = numeros[posicion]
            tipo = tipos[posicion]
            print('El pokemon', nombres[i], 'tiene el numero', numero, 'y es de tipo', tipo)


#APARTADO C:

#Mostramos TODOS los pokemon que sean de un tipo determinado:
#def mostrar_pokemon_tipo(tipo, tipos):
 #TODO: hacer esta funciom


#APARTADO D:

#Realizar un listado en orden ascendente por numero
#inorden(raiz2)

#Realizar un listado en orden ascendente por nombre
#inorden(raiz)
#Listado por nivel por nombre
#por_nivel(raiz)



#APARTADO E:

#Mostra todos los pokemons que son debiles frente a Jolteon(es decir, que tengan Electric en su lista de debilidades), Lycanroc (es decir, que tengan Fighting en su lista de debilidades) y Tyranrum (es decir, que tengan Dragon en su lista de debilidades).

def debil(Jolteon, Lycanroc, Tyrantrum):
    for i in range(len(tipos)):
        if 'Electric' in tipos[i]:
            posicion = tipos.index(tipos[i])
            nombre = nombres[posicion]
            numero = numeros[posicion]
            print('El pokemon', nombre, 'tiene el numero', numero, 'y es debil frente a Jolteon')
        if 'Fighting' in tipos[i]:
            posicion = tipos.index(tipos[i])
            nombre = nombres[posicion]
            numero = numeros[posicion]
            print('El pokemon', nombre, 'tiene el numero', numero, 'y es debil frente a Lycanroc')
        if 'Dragon' in tipos[i]:
            posicion = tipos.index(tipos[i])
            nombre = nombres[posicion]
            numero = numeros[posicion]
            print('El pokemon', nombre, 'tiene el numero', numero, 'y es debil frente a Tyrantrum')

#APARTADO F:

#mostrar todos los pokemons hay en el arbol

def mostrar_pokemons(raiz):
    if raiz != None:
        mostrar_pokemons(raiz.izq)
        print(raiz.info)
        mostrar_pokemons(raiz.der)

#mostramos la cantidad de pokemons que hay en el arbol
def valores_unicos(raiz3, unicos):
    '''Funcion que nos devuelve la cantidad de valores unicos que hay en el arbol'''
    if raiz3 is not None:
        if raiz3.info not in unicos:
            unicos[raiz3.info] = 1
        else:
            unicos[raiz3.info] = unicos[raiz3.info] + 1
        unicos = valores_unicos(raiz3.izq, unicos) #recorremos el arbol por la izquierda
        unicos = valores_unicos(raiz3.der, unicos) #recorremos el arbol por la derecha
    return unicos


