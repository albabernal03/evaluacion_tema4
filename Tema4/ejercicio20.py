import csv 

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
debilidades= []
for i in range(1, len(lista)): 
    debilidades.append(lista[i][2]) #Cogemos la columna 2 que es la de las debilidades


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

#DEBILIDADES:
raiz3 = None
for i in range(len(debilidades)):
    raiz3 = insertar_nodo(raiz3, debilidades[i])


#APARTADO B:

#mostrar todos los datos de un Pokémon a partir de su número

def mostrar_datos(numero):
    '''Funcion que nos imprime los datos de un pokemon a partir de su numero'''
    pos = buscar(raiz2, numero)
    if pos != None:
        print('El pokemon con el numero', numero, 'es', pos.izq.info, 'y su debilidad es', pos.der.info)
    else:
        print('El numero no esta en el arbol')
        